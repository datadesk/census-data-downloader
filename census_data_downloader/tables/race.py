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
        '001E': "universe",
        '003E': "white_alone",
        '004E': "black_alone",
        '005E': "american_indian_and_alaska_native",
        '006E': "asian_alone",
        '007E': "native_hawaiian_and_pacific_islander",
        '008E': "other_alone",
        '009E': "two_or_more_races",
        '012E': "latino_alone"
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
        "001E": "universe"
    })
