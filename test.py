import pathlib
import unittest
from unittest import mock
from us import states
import collections
import census_data_downloader
from click.testing import CliRunner
from census_data_downloader import cli


class CensusDataDownloaderTest(unittest.TestCase):
    THIS_DIR = pathlib.Path(__file__).parent

    def test_allyears(self):
        all = census_data_downloader.MedianGrossRentDownloader(
            years="all",
            data_dir="./test-data/"
        )
        all.download_nationwide()

    def test_multipleyears(self):
        multi = census_data_downloader.PopulationDownloader(
            years=[2009, 2017],
            data_dir="./test-data/"
        )
        multi.download_nationwide()


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

    def test_tracts(self):
        self.invoke("--data-dir", "./test-data/", "medianhouseholdincome", "tracts", "RI")
        self.invoke("--year", "2009", "--data-dir", "./test-data/", "medianhouseholdincome", "tracts", "RI")

    def test_varyingcrosswalksbyyear(self):
        self.invoke("--year", "2009", "--data-dir", "./test-data/", "yearstructurebuilt", "nationwide")
        self.invoke("--year", "2012", "--data-dir", "./test-data/", "yearstructurebuilt", "nationwide")
        self.invoke("--year", "2017", "--data-dir", "./test-data/", "yearstructurebuilt", "nationwide")


@mock.patch('census_data_downloader.PopulationDownloader._download_tables')
class GeographyTests(unittest.TestCase):
    NATIONAL_GEOGRAPHIES = (
        'us:1',
        'state:*',
        'congressional district:*',
        'county:*',
        'place:*',
        'urban area:*',
        'metropolitan statistical area/micropolitan statistical area:*',
        'combined statistical area:*',
        'public use microdata area:*',
        'american indian area/alaska native area/hawaiian home land:*',
        'zip code tabulation area:*'
    )
    STATE_GEOGRAPHIES = (
        'state legislative district (upper chamber):*',
        'state legislative district (lower chamber):*',
        'tract:*'
    )
    
    def test_usa(self, download_tables_mock):
        census_data_downloader.PopulationDownloader().download_usa()
        
        for geo in self.NATIONAL_GEOGRAPHIES:
            download_tables_mock.assert_any_call({'for': geo}, mock.ANY, mock.ANY)
        
        assert download_tables_mock.call_count == len(self.NATIONAL_GEOGRAPHIES)

    def test_everything(self, download_tables_mock):
        census_data_downloader.PopulationDownloader().download_everything()

        for geo in self.NATIONAL_GEOGRAPHIES:
            download_tables_mock.assert_any_call({'for': geo}, mock.ANY, mock.ANY)

        for geo in self.STATE_GEOGRAPHIES:
            for state in states.STATES:
                download_tables_mock.assert_any_call({'for': geo, 'in': f'state: {state.fips}'}, mock.ANY, mock.ANY)

        assert download_tables_mock.call_count == len(self.NATIONAL_GEOGRAPHIES) + len(self.STATE_GEOGRAPHIES) * len(states.STATES)

    def test_usa_limited(self, download_tables_mock):
        downloader = census_data_downloader.PopulationDownloader()
        downloader.GEO_LIST = ("nationwide", "states", "counties", "places")
        downloader.download_usa()

        download_tables_mock.assert_any_call({'for': 'us:1'}, mock.ANY, mock.ANY)
        download_tables_mock.assert_any_call({'for': 'state:*'}, mock.ANY, mock.ANY)
        download_tables_mock.assert_any_call({'for': 'county:*'}, mock.ANY, mock.ANY)
        download_tables_mock.assert_any_call({'for': 'place:*'}, mock.ANY, mock.ANY)

        assert download_tables_mock.call_count == 4

    def test_everything_limited(self, download_tables_mock):
        downloader = census_data_downloader.PopulationDownloader()
        downloader.GEO_LIST = tuple(set(downloader.GEO_LIST) - set(('state_legislative_districts_upper', 'state_legislative_districts_lower')))
        downloader.download_everything()

        for geo in self.NATIONAL_GEOGRAPHIES:
            download_tables_mock.assert_any_call({'for': geo}, mock.ANY, mock.ANY)

        for state in states.STATES:
            download_tables_mock.assert_any_call({'for': 'tract:*', 'in': f'state: {state.fips}'}, mock.ANY, mock.ANY)

        assert download_tables_mock.call_count == len(self.NATIONAL_GEOGRAPHIES) + len(states.STATES)

    def test_geo_methods(self, download_tables_mock):
        downloader = census_data_downloader.PopulationDownloader()
        downloader.GEO_LIST = ()

        self.assertRaises(NotImplementedError, downloader.download_nationwide)
        self.assertRaises(NotImplementedError, downloader.download_states)
        self.assertRaises(NotImplementedError, downloader.download_counties)
        self.assertRaises(NotImplementedError, downloader.download_congressional_districts)
        self.assertRaises(NotImplementedError, downloader.download_places)
        self.assertRaises(NotImplementedError, downloader.download_pumas)
        self.assertRaises(NotImplementedError, downloader.download_msas)
        self.assertRaises(NotImplementedError, downloader.download_csas)
        self.assertRaises(NotImplementedError, downloader.download_urban_areas)
        self.assertRaises(NotImplementedError, downloader.download_zctas)
        self.assertRaises(NotImplementedError, downloader.download_aiann_homelands)
        self.assertRaises(NotImplementedError, downloader.download_state_legislative_districts_lower, 'AL')
        self.assertRaises(NotImplementedError, downloader.download_state_legislative_districts_upper, 'AL')
        self.assertRaises(NotImplementedError, downloader.download_tracts, 'AL')

        download_tables_mock.assert_not_called()


if __name__ == '__main__':
    unittest.main()
