import pathlib
import unittest
from unittest import mock
from us import states
import pandas as pd
from pandas.util.testing import assert_series_equal
import collections
import census_data_downloader
from census_data_downloader import tables
from click.testing import CliRunner
from census_data_downloader import cli


class CensusDataDownloaderTest(unittest.TestCase):
    THIS_DIR = pathlib.Path(__file__).parent

    def test_allyears(self):
        all = tables.MedianGrossRentDownloader(
            years="all",
            data_dir="./test-data/"
        )
        all.download_nationwide()

    def test_multipleyears(self):
        multi = tables.PopulationDownloader(
            years=[2009, 2017],
            data_dir="./test-data/"
        )
        multi.download_nationwide()

    def test_moe_aggregator(self):
        internet = tables.InternetDownloader(
            years=[2017],
            data_dir="./test-data/"
        )
        internet.download_nationwide()
        test_data=pd.read_csv("./test-data/processed/acs5_2017_internet_nationwide.csv")
        self.assertEqual(test_data['total_no_internet_and_no_subscription'][0], 25279458)
        self.assertAlmostEqual(test_data['total_no_internet_and_no_subscription_moe'][0], 85272.1868,places=4)

class CliTest(unittest.TestCase):

    def invoke(self, *args):
        runner = CliRunner()
        result = runner.invoke(cli.cmd, args)
        print(result.output)
        self.assertEqual(result.exit_code, 0)
        string_value = result.output.replace("\n", "")
        return string_value

    def test_nationwide(self):
        self.invoke("--data-dir", "./test-data/", "medianhouseholdincome", "nationwide")
        self.invoke("--force", "--data-dir", "./test-data/", "medianhouseholdincome", "nationwide")

    def test_states(self):
        self.invoke("--data-dir", "./test-data/", "medianhouseholdincome", "states")

    # def test_tracts(self):
    #     self.invoke("--data-dir", "./test-data/", "medianhouseholdincome", "tracts")
    #     self.invoke("--year", "2009", "--data-dir", "./test-data/", "medianhouseholdincome", "tracts")

    # def test_varyingcrosswalksbyyear(self):
    #     self.invoke("--year", "2009", "--data-dir", "./test-data/", "yearstructurebuilt", "nationwide")
    #     self.invoke("--year", "2012", "--data-dir", "./test-data/", "yearstructurebuilt", "nationwide")
    #     self.invoke("--year", "2017", "--data-dir", "./test-data/", "yearstructurebuilt", "nationwide")


if __name__ == '__main__':
    unittest.main()
