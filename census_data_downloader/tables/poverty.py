import collections
from census_data_downloader.core.tables import BaseTableConfig
from census_data_downloader.core.decorators import register



@register
class PovertyDownloader(BaseTableConfig):
    """
#   This table is simplified downloader for the poverty table (B17001). 
    
    There are more variables that break down poverty by age, but this is the simplified version if you want the basics.
    """
    YEAR_LIST = (2017,)
    PROCESSED_TABLE_NAME = "poverty"
    UNIVERSE = "population"
    RAW_TABLE_NAME = 'B17001'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        '001E': 'universe',
        '002E': 'income_past12months_below_poverty_level',
        '031E': 'income_past12months_at_or_below_poverty_level'
    })
