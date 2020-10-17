# NOTE - THIS ISN'T COMPLETE FOR A REASON! IT'S JUST TO GIVE YOU AN IDEA ABOUT WHAT YOU CAN DO FOR TESTING
# You do not have to use this, it's mainly for inspiration

import boto3
from moto import mock_s3
from unittest import TestCase

from luigi.mock import MockTarget

@mock_s3
class LuigiDownloadTests(TestCase):

    def setUp(self):
        client = boto3.client("some_stuff")
        client.create_bucket("...")

    def tearDown(self):
        s3 = boto3.resource("....")
        # delete stuff from bucket

    def test_download_image(self):
        with TemporaryDirectory() as tmpdir:
            my_fake_file = "asdf.jpg"

            # upload fake image file to s3 bucket

            mock_output = MockTarget("...")

            class MockDownloadImage(MyPSET4Task):
                # Essentially here I want to override the output thanks to inheritance! Change this to a mock output instead
                def output(self):
                    return ...

            run_task(MockDownloadImage(filename="..."))

            self.assertTrue(mock_output.exists())

@mock_s3
class LuigiTestStylize(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_stylize(self):

        class MockStylize(MyPSET4Task):
            """
            You don't necessarily have to run the stylize if you don't need to, just verify file is generated

            Or you can try generating a fake image (much harder)
            """
            def program_args(self):
                return ["touch", "..."]