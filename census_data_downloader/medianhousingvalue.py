#! /usr/bin/env python
# -*- coding: utf-8 -*
import collections
from .base import BaseDownloader
from .registry import register_downloader


@register_downloader
class MedianHousingValueDownloader(BaseDownloader):
    PROCESSED_TABLE_NAME = "medianhousingvalue"
    RAW_TABLE_NAME = 'B25077'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        "001E": "median"
    })
