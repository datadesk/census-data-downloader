#! /usr/bin/env python
# -*- coding: utf-8 -*
import collections
from .base import BaseDownloader
from .registry import register_downloader


@register_downloader
class ForeignBornDownloader(BaseDownloader):
    PROCESSED_TABLE_NAME = "foreignborn"
    UNIVERSE = "total population"
    RAW_TABLE_NAME = 'B05002'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        "001E": "universe",
        "002E": "native",
        "013E": "foreign_born"
    })
