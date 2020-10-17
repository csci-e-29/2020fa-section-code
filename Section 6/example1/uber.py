import folium
import pandas as pd
from luigi import LocalTarget, Task
from luigi.contrib.external_program import ExternalProgramTask
from luigi.parameter import Parameter
from luigi.util import inherits
from luigi.task import flatten
from hashlib import sha256

"""
Steps to run:

1. PYTHONPATH="." luigi --module uber CreateUberDrive --local-scheduler  # run the luigi task once through
2. Try changing the versions and re-running! Rerun PYTHONPATH="." luigi --module uber CreateUberDrive --local-scheduler after changing the version(s) 

"""
# the below comes from professor gorlin's salted_demo
def get_salted_version(task):
    """Create a salted id/version for this task and lineage

    :returns: a unique, deterministic hexdigest for this task
    :rtype: str
    """

    msg = ""

    # Salt with lineage
    for req in flatten(task.requires()):
        # Note that order is important and impacts the hash - if task
        # requirements are a dict, then consider doing this is sorted order
        msg += get_salted_version(req)

    # Uniquely specify this task
    msg += ','.join([

            # Basic capture of input type
            task.__class__.__name__,

            # Change __version__ at class level when everything needs rerunning!
            task.__version__,

        ] + [
            # Depending on strictness - skipping params is acceptable if
            # output already is partitioned by their params; including every
            # param may make hash *too* sensitive
            '{}={}'.format(param_name, repr(task.param_kwargs[param_name]))
            for param_name, param in sorted(task.get_params())
            if param.significant
        ]
    )
    return sha256(msg.encode()).hexdigest()


def salted_target(task, file_pattern, format=None, **kwargs):
    """A local target with a file path formed with a 'salt' kwarg

    :rtype: LocalTarget
    """
    return LocalTarget(file_pattern.format(
        salt=get_salted_version(task)[:6], self=task, **kwargs
    ), format=format)


class FetchUberData(ExternalProgramTask):  # Note this points to an external task, aka something that exists outside of the pipeline we've created
    __version__ = '0.0.0'  # let's use semantic versioning to denote the version
    file_date = Parameter(default="apr-14")  # represents a date, so assume that we might have various days of data

    def program_args(self):
        return ["bash", "./download_data.sh", self.output().path]  # in this case executes a shell command

    def output(self):
        # return LocalTarget(self.file_output_name)
        return salted_target(self, self.file_date + "-uber-data-{salt}.csv")  # change the name of the output file to include the salt


@inherits(FetchUberData)  # inherits all the parameters from FetchUberData!
class PreprocessData(Task):
    __version__ = '0.0.0'  # let's use semantic versioning to denote the version

    def requires(self):  # requires creates the lineage of tasks -- i.e. in order to run this task, FetchUberData has to be complete
        return self.clone(FetchUberData)

    def run(self):  # define a run function, aka what this task wants to accomplish
        with self.input().open() as f:
            df = pd.read_csv(f)

        df["Date/Time"] = pd.to_datetime(df["Date/Time"])
        df = df.head(100)

        with self.output().open('w') as w:
            df[df["Base"] == df["Base"].sample(1).values[0]].to_csv(w, index=False)

    def output(self):  # define an output for this task (the data artifact that is created)
        return salted_target(self, "preprocessed-{salt}.csv")


@inherits(PreprocessData)
class CreateUberDrive(Task):
    __version__ = '0.0.0'  # let's use semantic versioning to denote the version

    def requires(self):
        return self.clone(PreprocessData)

    def run(self):
        with self.input().open() as f:
            df = pd.read_csv(f)

        sample_map = folium.Map(location=[df.iloc[0]['Lat'], df.iloc[0]['Lon']], tiles="Stamen Toner")
        points_list = list(zip(df['Lat'], df['Lon']))[0:1000]
        for i in range(len(points_list)):
             folium.CircleMarker(points_list[i], color="#ff7f00", radius=1).add_to(sample_map)
        sample_map.save(self.output().path)

    def output(self):
        return salted_target(self, "uber_drive-{salt}.html")


