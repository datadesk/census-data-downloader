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
    RAW_TABLE_NAME = 'B28002'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        '001E': 'universe',
        '002E': 'total_with_internet_subscription',
        '003E': 'dialup_internet_with_no_other_internet',
        '004E': 'broadband_internet',
        '005E': 'cellular_data',
        '006E': 'cellular_data_with_no_other_internet',
        '007E': 'total_with_internet_subscription_broadband',
        '008E': 'with_internet_subscription_broadband_with_no_other_internet',
        '009E': 'with_internet_satellite',
        '010E': 'with_internet_satellite_with_no_other_internet',
        '011E': 'with_internet_other_service_no_other_internet',
        '012E': 'internet_access_without_a_subscription',
        '013E': 'no_internet_access',  
    })