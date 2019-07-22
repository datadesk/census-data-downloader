#! /usr/bin/env python
# -*- coding: utf-8 -*
import collections
from pprint import pprint
import census_data_aggregator
from census_data_downloader.core import MOE_MAP
from census_data_downloader.core.tables import BaseTableConfig
from census_data_downloader.core.decorators import register


@register
class RaceDownloader(BaseTableConfig):
    PROCESSED_TABLE_NAME = "race"
    UNIVERSE = "total population"
    RAW_TABLE_NAME = 'B03002'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        '001': "universe",
        '003': "white_alone",
        '004': "black_alone",
        '005': "american_indian_and_alaska_native",
        '006': "asian_alone",
        '007': "native_hawaiian_and_pacific_islander",
        '008': "other_alone",
        '009': "two_or_more_races",
        '012': "latino_alone"
    })

    def process(self, df):
        # Our custom race groups
        def calculate_asians_moe(row):
            pprint(row)
            if row['asian_alone_moe'] in list(MOE_MAP.values()):
                value = sum([row['asian_alone'], row['native_hawaiian_and_pacific_islander']])
                moe = None
            value, moe = census_data_aggregator.approximate_sum(
                (row['native_hawaiian_and_pacific_islander'], row['native_hawaiian_and_pacific_islander_moe']),
                (row['asian_alone'], row['asian_alone_moe']),
            )
            row['asians_all'] = value
            row['asians_all_moe'] = moe
            return row

        df = df.apply(
            calculate_asians_moe,
            axis=1
        )

        def calculate_other_moe(row):
            pprint(row)
            if row['american_indian_and_alaska_native_moe'] in list(MOE_MAP.values()):
                value = sum([row['american_indian_and_alaska_native'], row['other_alone'], row['two_or_more_races']])
                moe = None
            value, moe = census_data_aggregator.approximate_sum(
                (row['american_indian_and_alaska_native'], row['american_indian_and_alaska_native_moe']),
                (row['other_alone'], row['other_alone_moe']),
                (row['two_or_more_races'], row['two_or_more_races_moe']),
            )
            row['other_all'] = value
            row['other_all_moe'] = moe
            return row

        df = df.apply(
            calculate_other_moe,
            axis=1
        )

        # Pass it back
        return df


@register
class AmericanIndianAlaskaNativeAloneOrInComboDownloader(BaseTableConfig):
    PROCESSED_TABLE_NAME = 'aianaloneorincombo'
    UNIVERSE = "people who are american indian or alaska native alone or in combination with one or more races"
    RAW_TABLE_NAME = 'B02010'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        "001": "universe"
    })


@register
class AsianDownloader(BaseTableConfig):
    PROCESSED_TABLE_NAME = "asian"
    UNIVERSE = "total asian alone population"
    RAW_TABLE_NAME = 'B02015'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        '001': "universe",
        '002': "asian_indian",
        '003': "bangladeshi",
        '004': "bhutanese",
        '005': "burmese",
        '006': "cambodian",
        '007': "chinese_except_taiwanese",
        '008': "filipino",
        '009': "hmong",
        '010': "indonesian",
        '011': "japanese",
        '012': "korean",
        '013': "laotian",
        '014': "malaysian",
        '015': "mongolian",
        '016': "nepalese",
        '017': "okinawan",
        '018': "pakistani",
        '019': "sri_lankan",
        '020': "taiwanese",
        '021': "thai",
        '022': "vietnamese",
        '023': "other_asian_specified",
        '024': "other_asian_not_specified",
        '025': "two_or_more_asian",
    })
