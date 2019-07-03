#! /usr/bin/env python
# -*- coding: utf-8 -*
import collections
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

    def process(self, *args, **kwargs):
        df = super().process(*args, **kwargs)
        # Our custom race groups
        df['asian_all'] = df['asian_alone'] + df['native_hawaiian_and_pacific_islander']
        df['other_all'] = df[[
            'american_indian_and_alaska_native',
            'other_alone',
            'two_or_more_races'
        ]].sum(axis=1)
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
