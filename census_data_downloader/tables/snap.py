#! /usr/bin/env python
# -*- coding: utf-8 -*
import collections
from census_data_downloader.core.tables import BaseTableConfig
from census_data_downloader.core.decorators import register


@register
class SnapbyPovertyDownloader(BaseTableConfig):
    """
    receipt of food stamps/snap in past 12 months by poverty status in the past 12 months for households
    """
    PROCESSED_TABLE_NAME = "snap"
    UNIVERSE = "households"
    RAW_TABLE_NAME = 'B22003'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        '001': "universe",
        '002': "received_snap_in_past_12_months",
        '003': "received_snap_in_past_12_months_income_below_poverty",
        '004': "received_snap_in_past_12_months_income_atorabove_poverty",
        '005': "not_received_snap_in_past_12_months",
        '006': "not_received_snap_in_past_12_months_income_below_poverty",
        '007': "not_received_snap_in_past_12_months_income_atorabove_poverty",
    })


@register
class SnapLatinoDownloader(BaseTableConfig):
    """
    receipt of food stamps/snap in past 12 months by race of householder
    """
    PROCESSED_TABLE_NAME = "snaplatino"
    RAW_TABLE_NAME = 'B22005I'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        '001': "universe",
        '002': "received_snap_in_past_12_months",
        '003': "not_received_snap_in_past_12_months"
    })


@register
class SnapWhiteDownloader(SnapLatinoDownloader):
    PROCESSED_TABLE_NAME = "snapwhite"
    RAW_TABLE_NAME = 'B22005H'


@register
class SnapBlackDownloader(SnapLatinoDownloader):
    PROCESSED_TABLE_NAME = "snapblack"
    RAW_TABLE_NAME = 'B22005B'


@register
class SnapAsianDownloader(SnapLatinoDownloader):
    PROCESSED_TABLE_NAME = "snapasian"
    RAW_TABLE_NAME = 'B22005D'
