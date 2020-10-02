import boto3
from moto import mock_s3

"""
An example to start to tie together a couple of things that we've talked about -- decorators, mocking, mixins, inheritance!
"""


class S3Mixin:

    @mock_s3  # mock is normally used for testing purposes so this is abusing moto, but at least for this example it's fine
    def save_data(self, my_text, file_name="fake.txt"):

        # the following is just syntax that creates a fake S3 bucket somewhere (note it's fake b/c we've used moto)
        conn = boto3.resource('s3', region_name='us-east-1')
        conn.create_bucket(Bucket='mybucket')

        # let's create a fake file with my_text in it
        object = conn.Object('mybucket', file_name)
        object.put(Body=my_text)

        # now we're pulling the file and seeing if we can read it in correctly
        body = conn.Object('mybucket', file_name).get()["Body"].read()
        print(body, "was saved onto S3")

        # In real life, this might be code that actually writes some data to s3 instead


class SpecializedMixin:
    # This is some other MixIn type - can be anything, but most of the time you want them to be very specialized.
    def custom_stuff_func(self, some_string):
        return ' '.join([some_string, "I needed to modify something"])


class MyClass(S3Mixin, SpecializedMixin):
    # Here I've inherited from two mixins, because I need functionality from both classes
    def run(self):
        boring_example = "Hello!"
        self.save_data(self.custom_stuff_func(boring_example))


m = MyClass()
m.run()
print(m.__class__.__mro__)
