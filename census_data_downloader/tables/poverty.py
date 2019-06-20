#! /usr/bin/env python
# -*- coding: utf-8 -*
import collections
from census_data_downloader.core.tables import BaseTableConfig
from census_data_downloader.core.decorators import register


@register
class PovertyDownloader(BaseTableConfig):
    """
    A simplified version of the poverty table that only returns grand totals.
    """
    PROCESSED_TABLE_NAME = "poverty"
    UNIVERSE = "population"
    RAW_TABLE_NAME = 'B17001'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        '001E': 'universe',
        '002E': 'income_past12months_below_poverty_level',
        '031E': 'income_past12months_at_or_above_poverty_level'
    })
