#! /usr/bin/env python
# -*- coding: utf-8 -*
import collections
from .base import BaseDownloader
from .registry import register_downloader


@register_downloader
class EducationDownloader(BaseDownloader):
    PROCESSED_TABLE_NAME = 'education'
    RAW_TABLE_NAME = 'B15002'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        '001E': "total",
        '002E': "male_total",
        '003E': "male_no_schooling",
        '004E': "male_nursery_to_4th_grade",
        '005E': "male_5th_and_6th_grade",
        '006E': "male_7th_and_8th_grade",
        '007E': "male_9th_grade",
        '008E': "male_10th_grade",
        '009E': "male_11th_grade",
        '010E': "male_12th_grade_no_diploma",
        '011E': "male_high_school_graduate",
        '012E': "male_less_than_1_year_college",
        '013E': "male_1_or_more_years_college",
        '014E': "male_associates_degree",
        '015E': "male_bachelors_degree",
        '016E': "male_masters_degree",
        '017E': "male_professional_school_degree",
        '018E': "male_doctorate_degree",
        '019E': "female_total",
        '020E': "female_no_schooling",
        '021E': "female_nursery_to_4th_grade",
        '022E': "female_5th_and_6th_grade",
        '023E': "female_7th_and_8th_grade",
        '024E': "female_9th_grade",
        '025E': "female_10th_grade",
        '026E': "female_11th_grade",
        '027E': "female_12th_grade_no_diploma",
        '028E': "female_high_school_graduate",
        '029E': "female_less_than_1_year_college",
        '030E': "female_1_or_more_years_college",
        '031E': "female_associates_degree",
        '032E': "female_bachelors_degree",
        '033E': "female_masters_degree",
        '034E': "female_professional_school_degree",
        '035E': "female_doctorate_degree",
    })

    def _process_raw_data(self, *args, **kwargs):
        """
        Combine raw age columns into our preferred groupings.
        """
        df = super()._process_raw_data(*args, **kwargs)

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
            "less_than_high_scool": [
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
