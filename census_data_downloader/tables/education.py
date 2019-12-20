#! /usr/bin/env python
# -*- coding: utf-8 -*
import collections
import census_data_aggregator
from census_data_downloader.core import MOE_MAP
from census_data_downloader.core.tables import BaseTableConfig
from census_data_downloader.core.decorators import register


@register
class EducationDownloader(BaseTableConfig):
    PROCESSED_TABLE_NAME = 'education'
    UNIVERSE = "population 25 Years and Over"
    RAW_TABLE_NAME = 'B15002'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        '001': "universe",
        '002': "male_total",
        '003': "male_no_schooling",
        '004': "male_nursery_to_4th_grade",
        '005': "male_5th_and_6th_grade",
        '006': "male_7th_and_8th_grade",
        '007': "male_9th_grade",
        '008': "male_10th_grade",
        '009': "male_11th_grade",
        '010': "male_12th_grade_no_diploma",
        '011': "male_high_school_graduate",
        '012': "male_less_than_1_year_college",
        '013': "male_1_or_more_years_college",
        '014': "male_associates_degree",
        '015': "male_bachelors_degree",
        '016': "male_masters_degree",
        '017': "male_professional_school_degree",
        '018': "male_doctorate_degree",
        '019': "female_total",
        '020': "female_no_schooling",
        '021': "female_nursery_to_4th_grade",
        '022': "female_5th_and_6th_grade",
        '023': "female_7th_and_8th_grade",
        '024': "female_9th_grade",
        '025': "female_10th_grade",
        '026': "female_11th_grade",
        '027': "female_12th_grade_no_diploma",
        '028': "female_high_school_graduate",
        '029': "female_less_than_1_year_college",
        '030': "female_1_or_more_years_college",
        '031': "female_associates_degree",
        '032': "female_bachelors_degree",
        '033': "female_masters_degree",
        '034': "female_professional_school_degree",
        '035': "female_doctorate_degree",
    })

    def process(self, df):
        """
        Combine raw age columns into our preferred groupings.
        """

        # Calculate totals for both genders together
        groups = [
            "no_schooling",
            "nursery_to_4th_grade",
            "5th_and_6th_grade",
            "7th_and_8th_grade",
            "9th_grade",
            "10th_grade",
            "11th_grade",
            "12th_grade_no_diploma",
            "high_school_graduate",
            "less_than_1_year_college",
            "1_or_more_years_college",
            "associates_degree",
            "bachelors_degree",
            "masters_degree",
            "professional_school_degree",
            "doctorate_degree",
        ]
        for g in groups:
            df[f'total_{g}'] = df[f'male_{g}'] + df[f'female_{g}']

        # Calculate our custom groups
        groupsets = collections.OrderedDict({
            "less_than_high_school": [
                "no_schooling",
                "nursery_to_4th_grade",
                "5th_and_6th_grade",
                "7th_and_8th_grade",
                "9th_grade",
                "10th_grade",
                "11th_grade",
                "12th_grade_no_diploma"
            ],
            "some_college": [
                "less_than_1_year_college",
                "1_or_more_years_college"
            ],
            "masters_or_higher": [
                "masters_degree",
                "professional_school_degree",
                "doctorate_degree"
            ],
            "bachelors_or_higher": [
                "bachelors_degree",
                "masters_degree",
                "professional_school_degree",
                "doctorate_degree"
            ]
        })
        for groupset, group_list in groupsets.items():
            df[f'total_{groupset}'] = df[[f'total_{f}' for f in group_list]].sum(axis=1)
            df[f'male_{groupset}'] = df[[f'male_{f}' for f in group_list]].sum(axis=1)
            df[f'female_{groupset}'] = df[[f'female_{f}' for f in group_list]].sum(axis=1)

        # Pass it back
        return df


@register
class EducationShortDownloader(BaseTableConfig):
    PROCESSED_TABLE_NAME = 'educationshort'
    UNIVERSE = "population 25 Years and Over"
    RAW_TABLE_NAME = 'B15002'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        '001': "universe",
        '015': "male_bachelors_degree",
        '016': "male_masters_degree",
        '017': "male_professional_school_degree",
        '018': "male_doctorate_degree",
        '032': "female_bachelors_degree",
        '033': "female_masters_degree",
        '034': "female_professional_school_degree",
        '035': "female_doctorate_degree",
    })

    def process(self, df):
        def calculate_male_bachelors_or_higher_moe(row):
            if row['male_bachelors_degree_moe'] in list(MOE_MAP.values()):
                value = sum([row['male_bachelors_degree'], row['male_masters_degree'], row['male_professional_school_degree'], row['male_doctorate_degree']])
                moe = None
            value, moe = census_data_aggregator.approximate_sum(
                (row['male_bachelors_degree'], row['male_bachelors_degree_moe']),
                (row['male_masters_degree'], row['male_masters_degree_moe']),
                (row['male_professional_school_degree'], row['male_professional_school_degree_moe']),
                (row['male_doctorate_degree'], row['male_doctorate_degree_moe'])
            )
            row['male_bachelors_or_higher'] = value
            row['male_bachelors_or_higher_moe'] = moe
            return row

        df = df.apply(
            calculate_male_bachelors_or_higher_moe,
            axis=1
        )

        def calculate_female_bachelors_or_higher_moe(row):
            if row['female_bachelors_degree_moe'] in list(MOE_MAP.values()):
                value = sum([row['female_bachelors_degree'], row['female_masters_degree'], row['female_professional_school_degree'], row['female_doctorate_degree']])
                moe = None
            value, moe = census_data_aggregator.approximate_sum(
                (row['female_bachelors_degree'], row['female_bachelors_degree_moe']),
                (row['female_masters_degree'], row['female_masters_degree_moe']),
                (row['female_professional_school_degree'], row['female_professional_school_degree_moe']),
                (row['female_doctorate_degree'], row['female_doctorate_degree_moe'])
            )
            row['female_bachelors_or_higher'] = value
            row['female_bachelors_or_higher_moe'] = moe
            return row

        df = df.apply(
            calculate_female_bachelors_or_higher_moe,
            axis=1
        )

        def calculate_total_bachelors_or_higher_moe(row):
            if row['female_bachelors_or_higher_moe'] in list(MOE_MAP.values()):
                value = sum([row['female_bachelors_or_higher'], row['male_bachelors_or_higher']])
                moe = None
            value, moe = census_data_aggregator.approximate_sum(
                (row['female_bachelors_degree'], row['female_bachelors_degree_moe']),
                (row['female_masters_degree'], row['female_masters_degree_moe']),
                (row['female_professional_school_degree'], row['female_professional_school_degree_moe']),
                (row['female_doctorate_degree'], row['female_doctorate_degree_moe']),
                (row['male_bachelors_degree'], row['male_bachelors_degree_moe']),
                (row['male_masters_degree'], row['male_masters_degree_moe']),
                (row['male_professional_school_degree'], row['male_professional_school_degree_moe']),
                (row['male_doctorate_degree'], row['male_doctorate_degree_moe'])
            )
            row['total_bachelors_or_higher'] = value
            row['total_bachelors_or_higher_moe'] = moe
            return row

        df = df.apply(
            calculate_total_bachelors_or_higher_moe,
            axis=1
        )

        # Pass it back
        return df
