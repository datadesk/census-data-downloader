import collections

ESTIMATE_MAP = collections.OrderedDict({
    "-999999999": "too few samples",
    "-888888888": "not applicable",
    "-666666666": "too few samples or ratio of medians cannot be calculated",
    "-555555555": "estimate is controlled",
    "-333333333": "falls in lowest interval or highest interval",
    "-222222222": "too few samples to calculate standard error",
    "*": "significantly different from most current year. C means controlled."
})
MOE_MAP = collections.OrderedDict({
    "N": "too few samples",
    "(X)": "not applicable",
    "-": "too few samples or ratio of medians cannot be calculated",
    "*****": "estimate is controlled",
    "***": "falls in lowest interval or highest interval",
    "**": "too few samples to calculate standard error",
    "+": "falls in the highest interval",
    "N/A": "significantly different from most current year. C means controlled"
})