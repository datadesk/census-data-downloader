#! /usr/bin/env python
# -*- coding: utf-8 -*
import collections
from .base import BaseDownloader
from .registry import register_downloader


@register_downloader
class InternetDownloader(BaseDownloader):
    YEAR_LIST = (2017,)
    PROCESSED_TABLE_NAME = "internet_subscription"
    UNIVERSE = "households"
    RAW_TABLE_NAME = 'B28002'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        '001E': 'universe',
        '001M': 'universe_moe',
        '002E': 'total_with_internet_subscription',
        '002M': 'total_with_internet_subscription_moe',
        '003E': 'dialup_internet_with_no_other_internet',
        '003M': 'dialup_internet_with_no_other_internet_moe',
        '004E': 'broadband_internet',
        '004M': 'broadband_internet_moe',
        '005E': 'cellular_data',
        '005M': 'cellular_data_moe',
        '006E': 'cellular_data_with_no_other_internet',
        '006M': 'cellular_data_with_no_other_internet_moe',
        '007E': 'total_with_internet_subscription_broadband',
        '007M': 'total_with_internet_subscription_broadband_moe',
        '008E': 'with_internet_subscription_broadband_with_no_other_internet',
        '008M': 'with_internet_subscription_broadband_with_no_other_internet_moe',
        '009E': 'with_internet_satellite',
        '009M': 'with_internet_satellite_moe',
        '010E': 'with_internet_satellite_with_no_other_internet',
        '010M': 'with_internet_satellite_with_no_other_internet_moe',
        '011E': 'with_internet_other_service_no_other_internet',
        '011M': 'with_internet_other_service_no_other_internet_moe',
        '012E': 'internet_access_without_a_subscription',
        '012M': 'internet_access_without_a_subscription',
        '013E': 'no_internet_access',
        '013M': 'no_internet_access_moe'     
    })
