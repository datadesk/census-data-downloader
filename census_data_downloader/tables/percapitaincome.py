#! /usr/bin/env python
# -*- coding: utf-8 -*
import collections
from census_data_downloader.core.tables import BaseTableConfig
from census_data_downloader.core.decorators import register


@register
class PerCapitaIncomeDownloader(BaseTableConfig):
    # inflation adjusted
    PROCESSED_TABLE_NAME = "percapitaincome"
    UNIVERSE = "total population"
    RAW_TABLE_NAME = 'B19301'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        '001': "per_capita_income"
    })


@register
class PerCapitaIncomeLatinoDownloader(PerCapitaIncomeDownloader):
    # inflation adjusted
    PROCESSED_TABLE_NAME = "percapitaincomelatino"
    RAW_TABLE_NAME = 'B19301I'


@register
class PerCapitaIncomeWhiteDownloader(PerCapitaIncomeDownloader):
    # inflation adjusted
    PROCESSED_TABLE_NAME = "percapitaincomewhite"
    RAW_TABLE_NAME = 'B19301H'


@register
class PerCapitaIncomeBlackDownloader(PerCapitaIncomeDownloader):
    # inflation adjusted
    PROCESSED_TABLE_NAME = "percapitaincomeblack"
    RAW_TABLE_NAME = 'B19301B'


@register
class PerCapitaIncomeAsianDownloader(PerCapitaIncomeDownloader):
    # inflation adjusted
    PROCESSED_TABLE_NAME = "percapitaincomeasian"
    RAW_TABLE_NAME = 'B19301D'
