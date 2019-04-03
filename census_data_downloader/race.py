#! /usr/bin/env python
# -*- coding: utf-8 -*
import collections
from .base import BaseDownloader
from .registry import register_downloader


@register_downloader
class RaceDownloader(BaseDownloader):
    PROCESSED_TABLE_NAME = "race"
    RAW_TABLE_NAME = 'B03002'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        '001E': "total",
        '003E': "white_alone",
        '004E': "black_alone",
        '005E': "american_indian_and_alaska_native",
        '006E': "asian_alone",
        '007E': "native_hawaiian_and_pacific_islander",
        '008E': "other_alone",
        '009E': "two_or_more_races",
        '012E': "latino_alone"
    })

    def _process_raw_data(self, *args, **kwargs):
        df = super()._process_raw_data(*args, **kwargs)
        # Our custom race groups
        df['asian_all'] = df['asian_alone'] + df['native_hawaiian_and_pacific_islander']
        df['other_all'] = df[[
            'american_indian_and_alaska_native',
            'other_alone',
            'two_or_more_races'
        ]].sum(axis=1)
        return df
