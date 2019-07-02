#! /usr/bin/env python
# -*- coding: utf-8 -*
import collections
from census_data_downloader.core.tables import BaseTableConfig
from census_data_downloader.core.decorators import register


@register
class EmploymentStatusDownloader(BaseTableConfig):
    PROCESSED_TABLE_NAME = "employmentstatus"
    UNIVERSE = "population 16 years and over"
    RAW_TABLE_NAME = 'B23025'
    YEAR_LIST = (
        2017,
        2016,
        2015,
        2014,
        2013,
        2012,
        2011
    )
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        '001': 'universe',
        '002': 'in_labor_force',
        '003': 'civilian',
        '004': 'civilian_employed',
        '005': 'civilian_unemployed',
        '006': 'armed_forces',
        '007': 'not_in_labor_force'
    })
