#! /usr/bin/env python
# -*- coding: utf-8 -*
import collections
import census_data_aggregator
from census_data_downloader.core import MOE_MAP
from census_data_downloader.core.tables import BaseTableConfig
from census_data_downloader.core.decorators import register


@register
class VoterEducationDownloader(BaseTableConfig):
    PROCESSED_TABLE_NAME = "voterbyeducation"
    """ citizen voting-age population by education level"""
    UNIVERSE = "citizens 18 years and over"
    RAW_TABLE_NAME = 'B29002'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        "001": "total",
        "002": "total_less_than_9_grade",
        "003": "total_9_12_no_diploma",
        "004": "total_high_school_grad",
        "005": "total_some_college_no_degree",
        "006": "total_associate_degree",
        "007": "total_bachelor_degree",
        "008": "total_graduate__or_professional_degree"
    })

    def process(self, df):
        def calculate_bachelors_or_higher_moe(row):
            if row['total_bachelor_degree_moe'] in list(MOE_MAP.values()):
                value = sum([row['total_bachelor_degree'], row['total_graduate__or_professional_degree']])
                moe = None
            value, moe = census_data_aggregator.approximate_sum(
                (row['total_bachelor_degree'], row['total_bachelor_degree_moe']),
                (row['total_graduate__or_professional_degree'], row['total_graduate__or_professional_degree_moe'])
            )
            row['total_bachelor_degree'] = value
            row['total_bachelor_degree_moe'] = moe
            return row

        df = df.apply(
            calculate_bachelors_or_higher_moe,
            axis=1
        )
