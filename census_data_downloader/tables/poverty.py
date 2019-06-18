import collections
from .base import BaseDownloader
from .registry import register_downloader


@register_downloader
class PovertyDownloader(BaseDownloader):
    YEAR_LIST = (2017,)
    PROCESSED_TABLE_NAME = "poverty_by_sex_and_age"
    UNIVERSE = "households"
    RAW_TABLE_NAME = 'B17001'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        '001E': 'universe',
        '002E': 'income_past12months_below_poverty_level',
        '003E': 'income_past12months_below_poverty_level_male',
        '017E': 'income_past12months_below_poverty_level_female',
        '031E': 'income_past12months_at_or_below_poverty_level',
    })

# This table is simplified downloader for the poverty table (B17001). There are more variables that break down poverty by age, but this is the simplified version if you want the basics.
