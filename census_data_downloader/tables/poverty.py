#! /usr/bin/env python
# -*- coding: utf-8 -*
import collections
from census_data_downloader.core.tables import BaseTableConfig
from census_data_downloader.core.decorators import register


@register
class PovertyDownloader(BaseTableConfig):
    """
    A simplified version of the poverty table that only returns grand totals.
    """
    PROCESSED_TABLE_NAME = "poverty"
    UNIVERSE = "population for whom poverty status is determined"
    RAW_TABLE_NAME = 'B17001'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        '001': 'universe',
        '002': 'income_past12months_below_poverty_level',
        '031': 'income_past12months_at_or_above_poverty_level'
    })


@register
class PovertyBySexDownloader(BaseTableConfig):
    """
    A simplified version of the poverty table that only returns totals by sex.
    """
    PROCESSED_TABLE_NAME = "povertystatusbygender"
    UNIVERSE = "population for whom poverty status is determined"
    RAW_TABLE_NAME = 'B17001'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        '001': "total",
        '002': "total_below_poverty_level",
        '003': "male_below_poverty_level",
        '017': "female_below_poverty_level",
        '031': "total_at_or_above_poverty_level",
        '032': "male_at_or_above_poverty_level",
        '046': "female_at_or_above_poverty_level"
    })


@register
class PovertyAgeDownloader(BaseTableConfig):
    """
    The full table.
    """
    PROCESSED_TABLE_NAME = "povertystatusbyage"
    UNIVERSE = "population for whom poverty status is determined"
    RAW_TABLE_NAME = 'B17001'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        '001': "total",
        '002': "total_below_poverty_level",
        '003': "male_below_poverty_level",
        '004': "male_under_5_below_poverty_level",
        '005': "male_5_below_poverty_level",
        '006': "male_6_to_11_below_poverty_level",
        '007': "male_12_to_14_below_poverty_level",
        '008': "male_15_below_poverty_level",
        '009': "male_16_to_17_below_poverty_level",
        '010': "male_18_to_24_below_poverty_level",
        '011': "male_25_to_34_below_poverty_level",
        '012': "male_35_to_44_below_poverty_level",
        '013': "male_45_to_54_below_poverty_level",
        '014': "male_55_to_64_below_poverty_level",
        '015': "male_65_to_74_below_poverty_level",
        '016': "male_75_and_over_below_poverty_level",
        '017': "female_below_poverty_level",
        '018': "female_under_5_below_poverty_level",
        '019': "female_5_below_poverty_level",
        '020': "female_6_to_11_below_poverty_level",
        '021': "female_12_to_14_below_poverty_level",
        '022': "female_15_below_poverty_level",
        '023': "female_16_to_17_below_poverty_level",
        '024': "female_18_to_24_below_poverty_level",
        '025': "female_25_to_34_below_poverty_level",
        '026': "female_35_to_44_below_poverty_level",
        '027': "female_45_to_54_below_poverty_level",
        '028': "female_55_to_64_below_poverty_level",
        '029': "female_65_to_74_below_poverty_level",
        '030': "female_75_and_over_below_poverty_level",
        '031': "total_at_or_above_poverty_level",
        '032': "male_at_or_above_poverty_level",
        '033': "male_under_5_at_or_above_poverty_level",
        '034': "male_5_at_or_above_poverty_level",
        '035': "male_6_to_11_at_or_above_poverty_level",
        '036': "male_12_to_14_at_or_above_poverty_level",
        '037': "male_15_at_or_above_poverty_level",
        '038': "male_16_to_17_at_or_above_poverty_level",
        '039': "male_18_to_24_at_or_above_poverty_level",
        '040': "male_25_to_34_at_or_above_poverty_level",
        '041': "male_35_to_44_at_or_above_poverty_level",
        '042': "male_45_to_54_at_or_above_poverty_level",
        '043': "male_55_to_64_at_or_above_poverty_level",
        '044': "male_65_to_74_at_or_above_poverty_level",
        '045': "male_75_and_over_at_or_above_poverty_level",
        '046': "female_at_or_above_poverty_level",
        '047': "female_under_5_at_or_above_poverty_level",
        '048': "female_5_at_or_above_poverty_level",
        '049': "female_6_to_11_at_or_above_poverty_level",
        '050': "female_12_to_14_at_or_above_poverty_level",
        '051': "female_15_at_or_above_poverty_level",
        '052': "female_16_to_17_at_or_above_poverty_level",
        '053': "female_18_to_24_at_or_above_poverty_level",
        '054': "female_25_to_34_at_or_above_poverty_level",
        '055': "female_35_to_44_at_or_above_poverty_level",
        '056': "female_45_to_54_at_or_above_poverty_level",
        '057': "female_55_to_64_at_or_above_poverty_level",
        '058': "female_65_to_74_at_or_above_poverty_level",
        '059': "female_75_and_over_at_or_above_poverty_level"
    })

    def process(self, df):

        # Calculate totals for both genders together
        groups = [
            'under_5_below_poverty_level',
            '5_below_poverty_level',
            '6_to_11_below_poverty_level',
            '12_to_14_below_poverty_level',
            '15_below_poverty_level',
            '16_to_17_below_poverty_level',
            '18_to_24_below_poverty_level',
            '25_to_34_below_poverty_level',
            '35_to_44_below_poverty_level',
            '45_to_54_below_poverty_level',
            '55_to_64_below_poverty_level',
            '65_to_74_below_poverty_level',
            '75_and_over_below_poverty_level',
            'under_5_at_or_above_poverty_level',
            '5_at_or_above_poverty_level',
            '6_to_11_at_or_above_poverty_level',
            '12_to_14_at_or_above_poverty_level',
            '15_at_or_above_poverty_level',
            '16_to_17_at_or_above_poverty_level',
            '18_to_24_at_or_above_poverty_level',
            '25_to_34_at_or_above_poverty_level',
            '35_to_44_at_or_above_poverty_level',
            '45_to_54_at_or_above_poverty_level',
            '55_to_64_at_or_above_poverty_level',
            '65_to_74_at_or_above_poverty_level',
            '75_and_over_at_or_above_poverty_level'
        ]
        for g in groups:
            df[f'total_{g}'] = df[f'male_{g}'] + df[f'female_{g}']

        # Calculate custom group sets
        groupsets = collections.OrderedDict({
            "0_to_17_total": [
                'under_5_below_poverty_level',
                '5_below_poverty_level',
                '6_to_11_below_poverty_level',
                '12_to_14_below_poverty_level',
                '15_below_poverty_level',
                '16_to_17_below_poverty_level',
                'under_5_at_or_above_poverty_level',
                '5_at_or_above_poverty_level',
                '6_to_11_at_or_above_poverty_level',
                '12_to_14_at_or_above_poverty_level',
                '15_at_or_above_poverty_level',
                '16_to_17_at_or_above_poverty_level',
            ],
            "0_to_17_below_poverty_level": [
                'under_5_below_poverty_level',
                '5_below_poverty_level',
                '6_to_11_below_poverty_level',
                '12_to_14_below_poverty_level',
                '15_below_poverty_level',
                '16_to_17_below_poverty_level',
            ],
            "18_to_34_total": [
                '18_to_24_below_poverty_level',
                '25_to_34_below_poverty_level',
                '18_to_24_at_or_above_poverty_level',
                '25_to_34_at_or_above_poverty_level',
            ],
            "18_to_34_below_poverty_level": [
                '18_to_24_below_poverty_level',
                '25_to_34_below_poverty_level',
            ],
            "35_to_64_total": [
                '35_to_44_below_poverty_level',
                '45_to_54_below_poverty_level',
                '55_to_64_below_poverty_level',
                '35_to_44_at_or_above_poverty_level',
                '45_to_54_at_or_above_poverty_level',
                '55_to_64_at_or_above_poverty_level',
            ],
            "35_to_64_below_poverty_level": [
                '35_to_44_below_poverty_level',
                '45_to_54_below_poverty_level',
                '55_to_64_below_poverty_level',
            ],
            "65_and_over_total": [
                '65_to_74_below_poverty_level',
                '75_and_over_below_poverty_level',
                '65_to_74_at_or_above_poverty_level',
                '75_and_over_at_or_above_poverty_level',
            ],
            "65_and_over_below_poverty_level": [
                '65_to_74_below_poverty_level',
                '75_and_over_below_poverty_level',
            ],
            "0_to_11_total": [
                '12_to_14_below_poverty_level',
                '15_below_poverty_level',
                '16_to_17_below_poverty_level',
                '12_to_14_at_or_above_poverty_level',
                '15_at_or_above_poverty_level',
                '16_to_17_at_or_above_poverty_level',
            ],
            "0_to_11_below_poverty_level": [
                '12_to_14_below_poverty_level',
                '15_below_poverty_level',
                '16_to_17_below_poverty_level',
            ],
            "12_to_17_total": [
                '12_to_14_below_poverty_level',
                '15_below_poverty_level',
                '16_to_17_below_poverty_level',
                '12_to_14_at_or_above_poverty_level',
                '15_at_or_above_poverty_level',
                '16_to_17_at_or_above_poverty_level',
            ],
            "12_to_17_below_poverty_level": [
                '12_to_14_below_poverty_level',
                '15_below_poverty_level',
                '16_to_17_below_poverty_level',
            ],
            "18_to_64_total": [
                '18_to_24_below_poverty_level',
                '25_to_34_below_poverty_level',
                '35_to_44_below_poverty_level',
                '45_to_54_below_poverty_level',
                '55_to_64_below_poverty_level',
                '18_to_24_at_or_above_poverty_level',
                '25_to_34_at_or_above_poverty_level',
                '35_to_44_at_or_above_poverty_level',
                '45_to_54_at_or_above_poverty_level',
                '55_to_64_at_or_above_poverty_level',
            ],
            "18_to_64_below_poverty_level": [
                '18_to_24_below_poverty_level',
                '25_to_34_below_poverty_level',
                '35_to_44_below_poverty_level',
                '45_to_54_below_poverty_level',
                '55_to_64_below_poverty_level',
            ]
        })
        for groupset, group_list in groupsets.items():
            df[f'total_{groupset}'] = df[[f'total_{f}' for f in group_list]].sum(axis=1)
            df[f'male_{groupset}'] = df[[f'male_{f}' for f in group_list]].sum(axis=1)
            df[f'female_{groupset}'] = df[[f'female_{f}' for f in group_list]].sum(axis=1)

        # Pass it back
        return df


@register
class PovertyLatinoDownloader(PovertyAgeDownloader):
    PROCESSED_TABLE_NAME = "povertylatino"
    RAW_TABLE_NAME = 'B17001I'
    UNIVERSE = "Latino population for whom poverty status is determined"


@register
class PovertyWhiteDownloader(PovertyAgeDownloader):
    PROCESSED_TABLE_NAME = "povertywhite"
    RAW_TABLE_NAME = 'B17001A'
    UNIVERSE = "white population for whom poverty status is determined"


@register
class PovertyBlackDownloader(PovertyAgeDownloader):
    PROCESSED_TABLE_NAME = "povertyblack"
    RAW_TABLE_NAME = 'B17001B'
    UNIVERSE = "Black population for whom poverty status is determined"


@register
class PovertyAsianDownloader(PovertyAgeDownloader):
    PROCESSED_TABLE_NAME = "povertyasian"
    RAW_TABLE_NAME = 'B17001D'
    UNIVERSE = "Asian population for whom poverty status is determined"
