#! /usr/bin/env python
# -*- coding: utf-8 -*
import collections
from census_data_downloader.core.tables import BaseTableConfig
from census_data_downloader.core.decorators import register


@register
class InternetDownloader(BaseTableConfig):
    YEAR_LIST = (2017,)
    PROCESSED_TABLE_NAME = "internet"
    UNIVERSE = "households"
    RAW_TABLE_NAME = 'B28003'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        '001E': 'universe',
        '002E': 'total_with_computer',
        '003E': 'dialup_internet',
        '004E': 'broadband_internet',
        '005E': 'computer_no_internet',
        '006E': 'total_no_computer'
    })

    def _process_raw_data(self, *args, **kwargs):
        df = super()._process_raw_data(*args, **kwargs)
        df['total_with_internet'] = df['dialup_internet'] + df['broadband_internet']
        df['total_no_internet'] = df['computer_no_internet'] + df['total_no_computer']
        return df
