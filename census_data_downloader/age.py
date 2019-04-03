#! /usr/bin/env python
# -*- coding: utf-8 -*
import collections
from .base import BaseDownloader
from .registry import register_downloader


@register_downloader
class AgeDownloader(BaseDownloader):
    PROCESSED_TABLE_NAME = "age"
    RAW_TABLE_NAME = 'B01001'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        '001E': "total",
        '002E': "male_total",
        '003E': "male_under_5",
        '004E': "male_5_to_9",
        '005E': "male_10_to_14",
        '006E': "male_15_to_17",
        '007E': "male_18_to_19",
        '008E': "male_20",
        '009E': "male_21",
        '010E': "male_22_to_24",
        '011E': "male_25_to_29",
        '012E': "male_30_to_34",
        '013E': "male_35_to_39",
        '014E': "male_40_to_44",
        '015E': "male_45_to_49",
        '016E': "male_50_to_54",
        '017E': "male_55_to_59",
        '018E': "male_60_to_61",
        '019E': "male_62_to_64",
        '020E': "male_65_to_66",
        '021E': "male_67_to_69",
        '022E': "male_70_to_74",
        '023E': "male_75_to_79",
        '024E': "male_80_to_84",
        '025E': "male_85_and_over",
        '026E': "female_total",
        '027E': "female_under_5",
        '028E': "female_5_to_9",
        '029E': "female_10_to_14",
        '030E': "female_15_to_17",
        '031E': "female_18_to_19",
        '032E': "female_20",
        '033E': "female_21",
        '034E': "female_22_to_24",
        '035E': "female_25_to_29",
        '036E': "female_30_to_34",
        '037E': "female_35_to_39",
        '038E': "female_40_to_44",
        '039E': "female_45_to_49",
        '040E': "female_50_to_54",
        '041E': "female_55_to_59",
        '042E': "female_60_to_61",
        '043E': "female_62_to_64",
        '044E': "female_65_to_66",
        '045E': "female_67_to_69",
        '046E': "female_70_to_74",
        '047E': "female_75_to_79",
        '048E': "female_80_to_84",
        '049E': "female_85_and_over"
    })

    def _process_raw_data(self, *args, **kwargs):
        df = super()._process_raw_data(*args, **kwargs)

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
