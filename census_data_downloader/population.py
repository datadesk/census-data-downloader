#! /usr/bin/env python
# -*- coding: utf-8 -*
import collections
from .base import BaseDownloader


class PopulationDownloader(BaseDownloader):
    PROCESSED_TABLE_NAME = "population"
    RAW_TABLE_NAME = 'B01003'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        "001E": "total"
    })
