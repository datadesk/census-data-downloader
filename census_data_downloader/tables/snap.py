#! /usr/bin/env python
# -*- coding: utf-8 -*
import collections
from census_data_downloader.core.tables import BaseTableConfig
from census_data_downloader.core.decorators import register


@register
class SnapbyPovertyDownloader(BaseTableConfig):
    """
    receipt of food stamps/snap in past 12 months by race of householder
    """
    PROCESSED_TABLE_NAME = "snap"
    UNIVERSE = "households"
    RAW_TABLE_NAME = 'B2203'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        '001': "per_capita_income"
    })


@register
class PerCapitaIncomeLatinoDownloader(PerCapitaIncomeDownloader):
    PROCESSED_TABLE_NAME = "percapitaincomelatino"
    RAW_TABLE_NAME = 'B2205I'


@register
class PerCapitaIncomeWhiteDownloader(PerCapitaIncomeDownloader):
    PROCESSED_TABLE_NAME = "percapitaincomewhite"
    RAW_TABLE_NAME = 'B2205H'


@register
class PerCapitaIncomeBlackDownloader(PerCapitaIncomeDownloader):
    PROCESSED_TABLE_NAME = "percapitaincomeblack"
    RAW_TABLE_NAME = 'B2205B'


@register
class PerCapitaIncomeAsianDownloader(PerCapitaIncomeDownloader):
    PROCESSED_TABLE_NAME = "percapitaincomeasian"
    RAW_TABLE_NAME = 'B2205D'
