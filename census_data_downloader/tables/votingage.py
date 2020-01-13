#! /usr/bin/env python
# -*- coding: utf-8 -*
import collections
from census_data_downloader.core.tables import BaseTableConfig
from census_data_downloader.core.decorators import register


@register
class VoterDownloader(BaseTableConfig):
    PROCESSED_TABLE_NAME = "voters"
    """ citizen voting-age population by age"""
    UNIVERSE = "citizens 18 years and over"
    RAW_TABLE_NAME = 'B29001'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        "001": "total",
        "002": "total_18_29_yrs_old",
        "003": "total_30_44_yrs_old",
        "004": "total_45_64_yrs_old",
        "005": "total_65_older"
    })
