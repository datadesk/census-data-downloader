#! /usr/bin/env python
# -*- coding: utf-8 -*
import collections
from .base import BaseDownloader
from .registry import register_downloader


@register_downloader
class MedianMonthlyHousingCostsDownloader(BaseDownloader):
    PROCESSED_TABLE_NAME = "medianmonthlyhousingcosts"
    RAW_TABLE_NAME = 'B25105'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        "001E": "median"
    })
