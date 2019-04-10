#! /usr/bin/env python
# -*- coding: utf-8 -*
import collections
from .base import BaseDownloader
from .registry import register_downloader


@register_downloader
class ClassOfWorkerDownloader(BaseDownloader):
    """
    Sex by Class of Worker for the Civilian Employed Population 16 Years and Over.
    """
    PROCESSED_TABLE_NAME = "classofworker"
    RAW_TABLE_NAME = 'B24080'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        '001E': "total",
        '002E': "male_total",
        '003E': "male_private_for_profit_wage_and_salary",
        '004E': "male_employee_of_private_company",
        '005E': "male_selfemployed_in_own_incorporated_business",
        '006E': "male_private_not_for_profit_wage_and_salary",
        '007E': "male_local_government",
        '008E': "male_state_government",
        '009E': "male_federal_government",
        '010E': "male_selfemployed_in_own_not_incorporated_business",
        '011E': "male_unpaid_family_workers",
        '012E': "female_total",
        '013E': "female_private_for_profit_wage_and_salary",
        '014E': "female_employee_of_private_company",
        '015E': "female_selfemployed_in_own_incorporated_business",
        '016E': "female_private_not_for_profit_wage_and_salary",
        '017E': "female_local_government",
        '018E': "female_state_government",
        '019E': "female_federal_government",
        '020E': "female_selfemployed_in_own_not_incorporated_business",
        '021E': "female_unpaid_family_workers"
    })

    def _process_raw_data(self, *args, **kwargs):
        df = super()._process_raw_data(*args, **kwargs)

        # Calculate totals for both genders together
        groups = [
            "private_for_profit_wage_and_salary",
            "employee_of_private_company",
            "selfemployed_in_own_incorporated_business",
            "private_not_for_profit_wage_and_salary",
            "local_government",
            "state_government",
            "federal_government",
            "selfemployed_in_own_not_incorporated_business",
            "unpaid_family_workers",
        ]
        for g in groups:
            df[f'total_{g}'] = df[f'male_{g}'] + df[f'female_{g}']

        # Calculate custom group sets
        groupsets = collections.OrderedDict({
            "government": [
                'local_government',
                'state_government',
                'federal_government',
            ],
        })
        for groupset, group_list in groupsets.items():
            df[f'total_{groupset}'] = df[[f'total_{f}' for f in group_list]].sum(axis=1)
            df[f'male_{groupset}'] = df[[f'male_{f}' for f in group_list]].sum(axis=1)
            df[f'female_{groupset}'] = df[[f'female_{f}' for f in group_list]].sum(axis=1)

        # Pass it back
        return df
