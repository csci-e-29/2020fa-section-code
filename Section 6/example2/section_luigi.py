import datetime
import luigi
import hashlib
import pprint

# Windows: set PYTHONPATH=%cd%;%PYTHONPATH%
# Mac: PYTHONPATH="." luigi --module section_luigi ReportStep --local-scheduler

""" 
Types of tasks:
    Task
    ExternalTask (S3, HDFS, etc)
    ExternalProgramTask (Luigi starts external program)
    
    Requires: specifies dependencies
    Output: specifies the output of the task
    Run: specifies the steps taken to run the task

"""


class InputWords(luigi.ExternalTask):
    def output(self):
        return luigi.LocalTarget("input_words.txt")


class InputNums(luigi.ExternalTask):
    def output(self):
        return luigi.LocalTarget("input_numbers.txt")


class AggregateStep(luigi.Task):
    def requires(self):
        return {
            'word': self.clone(InputWords),
            'nums': self.clone(InputNums)
        }

    def output(self):
        return luigi.LocalTarget("aggregated_data.txt")

    def run(self):
        with open(self.input()['word'].path, 'r') as infile:
            words = infile.read().splitlines()
        with open(self.input()['nums'].path, 'r') as numfile:
            nums = numfile.read().splitlines()
        words_nums_dict = dict(zip(words, nums))
        with self.output().open('w') as out_file:
            pprint.pprint(words_nums_dict, out_file)
        out_file.close()


class MapStep(luigi.Task):
    def requires(self):
        return self.clone(AggregateStep)

    def output(self):
        return luigi.LocalTarget("mapped_data.txt")

    def run(self):
        with self.output().open('w') as out_file:
            date_string = str(datetime.datetime.now())
            out_file.write(date_string + "\n")


class ReduceStep(luigi.Task):
    file_stem_reduce = luigi.Parameter(default='reduced_data')

    def requires(self):
        return MapStep()

    def output(self):
        return luigi.LocalTarget("{}.txt".format(self.file_stem_reduce))

    def run(self):
        with self.input().open('r') as infile:
            listofthings = str(infile.read().splitlines())
        with self.output().open('w') as out_file:
            out_file.write(listofthings)


class ReportStep(luigi.Task):
    file_stem_report = luigi.Parameter(default='reported_data')

    def requires(self):
        return ReduceStep()

    def output(self):
        return luigi.LocalTarget("{}.txt".format(self.file_stem_report))

    def run(self):
        with self.output().open('w') as out_file:
            date_string = str(datetime.datetime.now())
            out_file.write(date_string + "\n")
