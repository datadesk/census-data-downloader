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
        '001E': 'universe',
        '002E': 'income_past12months_below_poverty_level',
        '031E': 'income_past12months_at_or_above_poverty_level'
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
        '001E': "total",
        '002E': "total_below_poverty_level",
        '003E': "male_below_poverty_level",
        '017E': "female_below_poverty_level",
        '031E': "total_at_or_above_poverty_level",
        '032E': "male_at_or_above_poverty_level",
        '046E': "female_at_or_above_poverty_level"
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
        '001E': "total",
        '002E': "total_below_poverty_level",
        '003E': "male_below_poverty_level",
        '004E': "male_under_5_below_poverty_level",
        '005E': "male_5_below_poverty_level",
        '006E': "male_6_to_11_below_poverty_level",
        '007E': "male_12_to_14_below_poverty_level",
        '008E': "male_15_below_poverty_level",
        '009E': "male_16_to_17_below_poverty_level",
        '010E': "male_18_to_24_below_poverty_level",
        '011E': "male_25_to_34_below_poverty_level",
        '012E': "male_35_to_44_below_poverty_level",
        '013E': "male_45_to_54_below_poverty_level",
        '014E': "male_55_to_64_below_poverty_level",
        '015E': "male_65_to_74_below_poverty_level",
        '016E': "male_75_and_over_below_poverty_level",
        '017E': "female_below_poverty_level",
        '018E': "female_under_5_below_poverty_level",
        '019E': "female_5_below_poverty_level",
        '020E': "female_6_to_11_below_poverty_level",
        '021E': "female_12_to_14_below_poverty_level",
        '022E': "female_15_below_poverty_level",
        '023E': "female_16_to_17_below_poverty_level",
        '024E': "female_18_to_24_below_poverty_level",
        '025E': "female_25_to_34_below_poverty_level",
        '026E': "female_35_to_44_below_poverty_level",
        '027E': "female_45_to_54_below_poverty_level",
        '028E': "female_55_to_64_below_poverty_level",
        '029E': "female_65_to_74_below_poverty_level",
        '030E': "female_75_and_over_below_poverty_level",
        '031E': "total_at_or_above_poverty_level",
        '032E': "male_at_or_above_poverty_level",
        '033E': "male_under_5_at_or_above_poverty_level",
        '034E': "male_5_at_or_above_poverty_level",
        '035E': "male_6_to_11_at_or_above_poverty_level",
        '036E': "male_12_to_14_at_or_above_poverty_level",
        '037E': "male_15_at_or_above_poverty_level",
        '038E': "male_16_to_17_at_or_above_poverty_level",
        '039E': "male_18_to_24_at_or_above_poverty_level",
        '040E': "male_25_to_34_at_or_above_poverty_level",
        '041E': "male_35_to_44_at_or_above_poverty_level",
        '042E': "male_45_to_54_at_or_above_poverty_level",
        '043E': "male_55_to_64_at_or_above_poverty_level",
        '044E': "male_65_to_74_at_or_above_poverty_level",
        '045E': "male_75_and_over_at_or_above_poverty_level",
        '046E': "female_at_or_above_poverty_level",
        '047E': "female_under_5_at_or_above_poverty_level",
        '048E': "female_5_at_or_above_poverty_level",
        '049E': "female_6_to_11_at_or_above_poverty_level",
        '050E': "female_12_to_14_at_or_above_poverty_level",
        '051E': "female_15_at_or_above_poverty_level",
        '052E': "female_16_to_17_at_or_above_poverty_level",
        '053E': "female_18_to_24_at_or_above_poverty_level",
        '054E': "female_25_to_34_at_or_above_poverty_level",
        '055E': "female_35_to_44_at_or_above_poverty_level",
        '056E': "female_45_to_54_at_or_above_poverty_level",
        '057E': "female_55_to_64_at_or_above_poverty_level",
        '058E': "female_65_to_74_at_or_above_poverty_level",
        '059E': "female_75_and_over_at_or_above_poverty_level"
    })

    def process(self, *args, **kwargs):
        df = super().process(*args, **kwargs)

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
