#! /usr/bin/env python
# -*- coding: utf-8 -*
import collections
from census_data_downloader.core.tables import BaseTableConfig
from census_data_downloader.core.decorators import register


@register
class VoterIncomeDownloader(BaseTableConfig):
    PROCESSED_TABLE_NAME = "voterbyincome"
    """ median household income for households with a citizen voting-age householder"""
    UNIVERSE = "citizens 18 years and over"
    RAW_TABLE_NAME = 'B29001'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        "001": "median"
    })
