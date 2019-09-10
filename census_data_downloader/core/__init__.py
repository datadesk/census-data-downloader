import collections

# https://www.census.gov/data/developers/data-sets/acs-1year/notes-on-acs-estimate-and-annotation-values.html

ESTIMATE_MAP = collections.OrderedDict({
    "-999999999": "too few samples",
    "-888888888": "not applicable",
    "-666666666": "estimate can't be calculated",
    "*": "significantly different from most current year",
    "C": "controlled so don't use tests",
    # "+": "",
    # "-": "falls in the lowest interval"
})
MOE_MAP = collections.OrderedDict({
    "N": "too few samples",
    "(X)": "not applicable",
    "-": "too few samples or ratio of medians cannot be calculated",
    "*****": "estimate is controlled",
    "***": "falls in lowest interval or highest interval",
    "**": "too few samples to calculate standard error",
    "-555555555": "estimate is controlled",
    "-333333333": "falls in lowest interval or highest interval",
    "-222222222": "too few samples to calculate standard error",
    "N/A": "significantly different from most current year"
})
