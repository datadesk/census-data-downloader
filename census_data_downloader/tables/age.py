#! /usr/bin/env python
# -*- coding: utf-8 -*
import collections
from census_data_downloader.core.tables import BaseTableConfig
from census_data_downloader.core.decorators import register


@register
class AgeDownloader(BaseTableConfig):
    PROCESSED_TABLE_NAME = "age"
    UNIVERSE = "total population"
    RAW_TABLE_NAME = 'B01001'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        '001': "universe",
        '002': "male_total",
        '003': "male_under_5",
        '004': "male_5_to_9",
        '005': "male_10_to_14",
        '006': "male_15_to_17",
        '007': "male_18_to_19",
        '008': "male_20",
        '009': "male_21",
        '010': "male_22_to_24",
        '011': "male_25_to_29",
        '012': "male_30_to_34",
        '013': "male_35_to_39",
        '014': "male_40_to_44",
        '015': "male_45_to_49",
        '016': "male_50_to_54",
        '017': "male_55_to_59",
        '018': "male_60_to_61",
        '019': "male_62_to_64",
        '020': "male_65_to_66",
        '021': "male_67_to_69",
        '022': "male_70_to_74",
        '023': "male_75_to_79",
        '024': "male_80_to_84",
        '025': "male_85_and_over",
        '026': "female_total",
        '027': "female_under_5",
        '028': "female_5_to_9",
        '029': "female_10_to_14",
        '030': "female_15_to_17",
        '031': "female_18_to_19",
        '032': "female_20",
        '033': "female_21",
        '034': "female_22_to_24",
        '035': "female_25_to_29",
        '036': "female_30_to_34",
        '037': "female_35_to_39",
        '038': "female_40_to_44",
        '039': "female_45_to_49",
        '040': "female_50_to_54",
        '041': "female_55_to_59",
        '042': "female_60_to_61",
        '043': "female_62_to_64",
        '044': "female_65_to_66",
        '045': "female_67_to_69",
        '046': "female_70_to_74",
        '047': "female_75_to_79",
        '048': "female_80_to_84",
        '049': "female_85_and_over"
    })

    def process(self, df):
        # Calculate totals for both genders together
        groups = [
            'under_5',
            '5_to_9',
            '10_to_14',
            '15_to_17',
            '18_to_19',
            '20',
            '21',
            '22_to_24',
            '25_to_29',
            '30_to_34',
            '35_to_39',
            '40_to_44',
            '45_to_49',
            '50_to_54',
            '55_to_59',
            '60_to_61',
            '62_to_64',
            '65_to_66',
            '67_to_69',
            '70_to_74',
            '75_to_79',
            '80_to_84',
            '85_and_over'
        ]
        for g in groups:
            df[f'total_{g}'] = df[f'male_{g}'] + df[f'female_{g}']

        # Calculate custom group sets
        groupsets = collections.OrderedDict({
            "0_to_17": [
                'under_5',
                '5_to_9',
                '10_to_14',
                '15_to_17',
            ],
            "5_to_17": [
                '5_to_9',
                '10_to_14',
                '15_to_17',
            ],
            "0_9": [
                'under_5',
                '5_to_9',
            ],
            "10_to_17": [
                '10_to_14',
                '15_to_17',
            ],
            "18_to_34": [
                '18_to_19',
                '20',
                '21',
                '22_to_24',
                '25_to_29',
                '30_to_34',
            ],
            "35_to_49": [
                '35_to_39',
                '40_to_44',
                '45_to_49',
            ],
            "50_to_64": [
                '50_to_54',
                '55_to_59',
                '60_to_61',
                '62_to_64',
            ],
            "65_and_over": [
                '65_to_66',
                '67_to_69',
                '70_to_74',
                '75_to_79',
                '80_to_84',
                '85_and_over'
            ]
        })
        for groupset, group_list in groupsets.items():
            df[f'total_{groupset}'] = df[[f'total_{f}' for f in group_list]].sum(axis=1)
            df[f'male_{groupset}'] = df[[f'male_{f}' for f in group_list]].sum(axis=1)
            df[f'female_{groupset}'] = df[[f'female_{f}' for f in group_list]].sum(axis=1)
        # Pass it back
        return df
