# census-data-downloader

Download Census data and reformat it for humans.

### Installation

```bash
$ pipenv install census-data-downloader
```

### Usage

Import our module.

```python
>>> import census_data_downloader
```

Download everything.

```
>>> census_data_downloader.download_everything("<YOUR CENSUS API KEY>", data_dir="./your-data-folder/")
```

That's it.

### Adding support for a new table

Subclass our downloader and provided it with its required inputs.

```python
import collections
from .base import BaseACSDownloader


class MedianHouseholdIncomeDownloader(BaseACSDownloader):
    PROCESSED_TABLE_NAME = "medianhouseholdincome"  # Your humanized table name
    RAW_TABLE_NAME = 'B19013'  # The id of the source table
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        # A crosswalk between the raw field name and our humanized field name.
        "001E": "median"
    })
```

Now you can import and run it yourself.

```python
>>> from yourmodule import MedianHouseholdIncomeDownloader
>>> obj = MedianHouseholdIncomeDownloader("<YOUR CENSUS API KEY>", data_dir="./your-data-folder/")
>>> obj.download_everything()
```

That's it. If you make some good ones, please consider submitting them as pull requests so everyone can benefit.

### Working with the data

All of the data files processed by this repository are published in the [processed data](./data/processed/) folder. They can be called in to applications via their raw URLs. Here are some examples created using [Observable](https://observablehq.com/collection/@datadesk/u-s-census-data).

Here's [county-level race data](https://github.com/datadesk/census-data-downloader/blob/master/data/processed/acs5_2017_race_counties.csv) in [a bivariate map](https://observablehq.com/@datadesk/black-and-latino-u-s-population-shares) of black and Latino populations.

[![Black and Latino U.S. population shares](./img/race-map.png)](https://observablehq.com/@datadesk/black-and-latino-u-s-population-shares)

Now [a stacked bar](https://observablehq.com/@datadesk/racial-makeup-of-u-s-states-and-territories) using the [state-level version](https://github.com/datadesk/census-data-downloader/blob/master/data/processed/acs5_2017_race_states.csv) of the race dataset.

[![Racial makeup  of U.S. states and territories](img/states-race-stacked-bar.png)](https://observablehq.com/@datadesk/racial-makeup-of-u-s-states-and-territories)

Datasets can be easily combined using the Census Bureau's `geoid` field. Here's [education and income by county](https://observablehq.com/@datadesk/education-and-income-in-u-s-counties) in a scatterplot with hexagonal bins.

[![Education and income in U.S. counties](img/hex-scatter.png)](https://observablehq.com/@datadesk/education-and-income-in-u-s-counties)

Lace a few more county-level datasets in and you can make [parallel coordinates charts](https://observablehq.com/@datadesk/the-demographics-and-destiny-of-all-3-220-u-s-counties).

[![The demographics and destiny of all 3,220 U.S. counties](img/parallel-coordinates.png)](https://observablehq.com/@datadesk/the-demographics-and-destiny-of-all-3-220-u-s-counties)
