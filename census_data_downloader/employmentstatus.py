#! /usr/bin/env python
# -*- coding: utf-8 -*
import collections
from .base import BaseDownloader
from .registry import register_downloader


@register_downloader
class EmploymentStatusDownloader(BaseDownloader):
    PROCESSED_TABLE_NAME = "employmentstatus"
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
        '001E': 'total_population_16over',
        '002E': 'in_labor_force',
        '003E': 'civilian',
        '004E': 'civilian_employed',
        '005E': 'civilian_unemployed',
        '006E': 'armed_forces',
        '007E': 'not_in_labor_force'
    })
