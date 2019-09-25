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
    RAW_TABLE_NAME = 'B2203'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        '001': "total",
        '002': "household_received_snap_in_past_12_months",
        '003': "household_received_snap_in_past_12_months_income_below_poverty",
        '004': "household_received_snap_in_past_12_months_income_atorabove_poverty",
        '005': "household_not_received_snap_in_past_12_months",
        '006': "household_not_received_snap_in_past_12_months_income_below_poverty",
        '007': "household_not_received_snap_in_past_12_months_income_atorabove_poverty",
    })


@register
class SnapLatinoDownloader(BaseTableConfig):
    """
    receipt of food stamps/snap in past 12 months by race of householder
    """
    PROCESSED_TABLE_NAME = "percapitaincomelatino"
    RAW_TABLE_NAME = 'B2205I'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        '001': "total",
        '002': "household_received_snap_in_past_12_months",
        '003': "household_not_received_snap_in_past_12_months"
    })


@register
class SnapWhiteDownloader(SnapLatinoDownloader):
    PROCESSED_TABLE_NAME = "percapitaincomewhite"
    RAW_TABLE_NAME = 'B2205H'


@register
class SnapBlackDownloader(SnapLatinoDownloader):
    PROCESSED_TABLE_NAME = "percapitaincomeblack"
    RAW_TABLE_NAME = 'B2205B'


@register
class SnapAsianDownloader(SnapLatinoDownloader):
    PROCESSED_TABLE_NAME = "percapitaincomeasian"
    RAW_TABLE_NAME = 'B2205D'
