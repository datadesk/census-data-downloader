import collections
from census_data_downloader.base import BaseDownloader


class MedianMonthlyHousingCostsDownloader(BaseDownloader):
    PROCESSED_TABLE_NAME = "medianmonthlyhousingcosts"
    RAW_TABLE_NAME = 'B25105'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        "001E": "median"
    })
