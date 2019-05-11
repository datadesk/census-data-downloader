#! /usr/bin/env python
# -*- coding: utf-8 -*
import collections
from .base import BaseDownloader
from .registry import register_downloader


@register_downloader
class MedianGrossRentDownloader(BaseDownloader):
    PROCESSED_TABLE_NAME = "mediangrossrent"
    UNIVERSE = "renter-occupied housing units paying cash rent"
    RAW_TABLE_NAME = 'B25064'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        "001E": "median"
    })
