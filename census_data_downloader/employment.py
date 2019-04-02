#! /usr/bin/env python
# -*- coding: utf-8 -*
import collections
from .base import BaseDownloader


class EmploymentDownloader(BaseDownloader):
    YEAR_LIST = (
        2017,
        2016,
        2015,
        2014,
        2013,
        2012,
        2011
    )
    PROCESSED_TABLE_NAME = "employment"
    RAW_TABLE_NAME = 'B23025'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        '001E': 'total_population_16over',
        '002E': 'in_labor_force',
        '003E': 'civilian',
        '004E': 'civilian_employed',
        '005E': 'civilian_unemployed',
        '006E': 'armed_forces',
        '007E': 'not_in_labor_force'
    })
