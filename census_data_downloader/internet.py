#! /usr/bin/env python
# -*- coding: utf-8 -*
import collections
from .base import BaseDownloader
from .registry import register_downloader


@register_downloader
class InternetDownloader(BaseDownloader):
    YEAR_LIST = (2017,)
    PROCESSED_TABLE_NAME = "internet"
    RAW_TABLE_NAME = 'B28003'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        '001E': 'total_households',
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
