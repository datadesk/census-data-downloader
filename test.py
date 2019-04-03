import pathlib
import unittest
import census_data_downloader
from click.testing import CliRunner
from census_data_downloader import cli


class CensusDataDownloaderTest(unittest.TestCase):
    THIS_DIR = pathlib.Path(__file__).parent

    def test_nothing(self):
        self.assertEqual(census_data_downloader, census_data_downloader)


class CliTest(unittest.TestCase):

    def invoke(self, *args):
        runner = CliRunner()
        result = runner.invoke(cli.cmd, args)
        self.assertEqual(result.exit_code, 0)
        string_value = result.output.replace("\n", "")
        return string_value

    def test_nationwide(self):
        self.invoke("--data-dir", "./test-data/", "medianhouseholdincome", "nationwide")
        self.invoke("--force", "--data-dir", "./test-data/", "medianhouseholdincome", "nationwide")

    def test_states(self):
        self.invoke("--data-dir", "./test-data/", "medianhouseholdincome", "states")

    def test_tracts(self):
        self.invoke("--data-dir", "./test-data/", "medianhouseholdincome", "tracts", "RI")
        self.invoke("--year", "2009", "--data-dir", "./test-data/", "medianhouseholdincome", "tracts", "RI")


if __name__ == '__main__':
    unittest.main()
