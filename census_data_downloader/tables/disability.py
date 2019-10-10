#! /usr/bin/env python
# -*- coding: utf-8 -*
import collections
from census_data_downloader.core.tables import BaseTableConfig
from census_data_downloader.core.decorators import register


@register
class DisabilityDownloader(BaseTableConfig):
    """
    Sex by age by disability status.
    https://factfinder.census.gov/help/en/civilian_noninstitutionalized_population.htm
    """
    PROCESSED_TABLE_NAME = "disability"
    UNIVERSE = "civilian noninstitutionalized population"
    RAW_TABLE_NAME = 'B18101'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        '001': "universe",
        '002': "male",
        '003': "male_under_5",
        '004': "male_under5_disability",
        '005': "male_under5_nodisability",
        '006': "male_5to17",
        '007': "male_5to17_disability",
        '008': "male_5to17_nodisability",
        '009': "male_18to34",
        '010': "male_18to34_disability",
        '011': "male_18to34_nodisability",
        '012': "male_35to64",
        '013': "male_35to64_disability",
        '014': "male_35to64_nodisability",
        '015': "male_65to74",
        '016': "male_65to74_disability",
        '017': "male_65to74_nodisability",
        '018': "male_75older",
        '019': "male_75older_disability",
        '020': "male_75older_nodisability",
        '021': "female",
        '022': "female_under_5",
        '023': "female_under5_disability",
        '024': "female_under5_nodisability",
        '025': "female_5to17",
        '026': "female_5to17_disability",
        '027': "female_5to17_nodisability",
        '028': "female_18to34",
        '029': "female_18to34_disability",
        '030': "female_18to34_nodisability",
        '031': "female_35to64",
        '032': "female_35to64_disability",
        '033': "female_35to64_nodisability",
        '034': "female_65to74",
        '035': "female_65to74_disability",
        '036': "female_65to74_nodisability",
        '037': "female_75older",
        '038': "female_75older_disability",
        '039': "female_75older_nodisability",
    })


@register
class DisabilityPovertyDownloader(BaseTableConfig):
    """
    Age by disability status by poverty status. Income in the past 12 months.
    https://factfinder.census.gov/help/en/civilian_noninstitutionalized_population.htm
    """
    PROCESSED_TABLE_NAME = "disabilitypoverty"
    UNIVERSE = "civilian noninstitutionalized population for whom poverty status is determined"
    RAW_TABLE_NAME = 'C18130'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        '001': "universe",
        '002': "under18",
        '003': "under18_disability",
        '004': "under18_disability_below_povertylevel",
        '005': "under18_disability_atorabove_povertylevel",
        '006': "under18_nodisability",
        '007': "under18_nodisability_below_povertylevel",
        '008': "under18_nodisability_atorabove_povertylevel",
        '009': "18to64",
        '010': "18to64_disability",
        '011': "18to64_disability_below_povertylevel",
        '012': "18to64_disability_atorabove_povertylevel",
        '013': "18to64_nodisability",
        '014': "18to64_nodisability_below_povertylevel",
        '015': "18to64_nodisability_atorabove_povertylevel",
        '016': "65older",
        '017': "65older_disability",
        '018': "65older_disability_below_povertylevel",
        '019': "65older_disability_atorabove_povertylevel",
        '020': "65older_nodisability",
        '021': "65older_nodisability_below_povertylevel",
        '022': "65older_nodisability_atorabove_povertylevel",
    })


@register
class CognitiveDifficultyDownloader(BaseTableConfig):
    """
    Sex by age by cognitive difficulty.
    https://factfinder.census.gov/help/en/civilian_noninstitutionalized_population.htm
    """
    PROCESSED_TABLE_NAME = "cognitivedifficulty"
    UNIVERSE = "civilian noninstitutionalized population 5 years or over"
    RAW_TABLE_NAME = 'B18104'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        '001': "universe",
        '002': "male",
        '003': "male_5_17",
        '004': "male_5_17_cognitive",
        '005': "male_5_17_nocognitive",
        '006': "male_18_34",
        '007': "male_18_34_cognitive",
        '008': "male_18_34_nocognitive",
        '009': "male_35_64",
        '010': "male_35_64_cognitive",
        '011': "male_35_64_nocognitive",
        '012': "male_65_74",
        '013': "male_65_74_cognitive",
        '014': "male_65_74_nocognitive",
        '015': "male_75_older",
        '016': "male_75_older_cognitive",
        '017': "male_75_older_nocognitive",
        '018': "female",
        '019': "female_5_17",
        '020': "female_5_17_cognitive",
        '021': "female_5_17_nocognitive",
        '022': "female_18_34",
        '023': "female_18_34_cognitive",
        '024': "female_18_34_nocognitive",
        '025': "female_35_64",
        '026': "female_35_64_cognitive",
        '027': "female_35_64_nocognitive",
        '028': "female_65_74",
        '029': "female_65_74_cognitive",
        '030': "female_65_74_nocognitive",
        '031': "female_75_older",
        '032': "female_75_older_cognitive",
        '033': "female_75_older_nocognitive",
    })
