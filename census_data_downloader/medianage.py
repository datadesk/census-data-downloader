#! /usr/bin/env python
# -*- coding: utf-8 -*
import collections
from .base import BaseDownloader
from .registry import register_downloader


@register_downloader
class MedianAgeDownloader(BaseDownloader):
    PROCESSED_TABLE_NAME = 'medianage'
    RAW_TABLE_NAME = 'B01002'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        "001E": "median",
        "002E": "male",
        "003E": "female"
    })
