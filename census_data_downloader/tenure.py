#! /usr/bin/env python
# -*- coding: utf-8 -*
import collections
from .base import BaseDownloader
from .registry import register_downloader


@register_downloader
class TenureDownloader(BaseDownloader):
    PROCESSED_TABLE_NAME = "tenure"
    RAW_TABLE_NAME = 'B25003'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        '001E': 'housing_units',
        '002E': 'owner_occupied',
        '003E': 'renter_occupied'
    })


@register_downloader
class TenureLatinoDownloader(TenureDownloader):
    PROCESSED_TABLE_NAME = "tenurelatino"
    RAW_TABLE_NAME = 'B25003I'


@register_downloader
class TenureWhiteDownloader(TenureDownloader):
    PROCESSED_TABLE_NAME = "tenurewhite"
    RAW_TABLE_NAME = 'B25003H'


@register_downloader
class TenureBlackDownloader(TenureDownloader):
    PROCESSED_TABLE_NAME = "tenureblack"
    RAW_TABLE_NAME = 'B25003B'


@register_downloader
class TenureAsianDownloader(TenureDownloader):
    PROCESSED_TABLE_NAME = "tenureasian"
    RAW_TABLE_NAME = 'B25003D'
