#! /usr/bin/env python
# -*- coding: utf-8 -*
TABLE_LIST = []


def register(cls):
    """
    A decorator to register new table configuration classes.
    """
    TABLE_LIST.append(cls)
    return cls


def downloader(func):
    """
    A decorator to download data for a downloader class.
    """
    def inner(*args, **kwargs):
        config = args[0]
        klass = func(config)
        for year in config.years_to_download:
            dl = klass(config, year)
            dl.download()
            dl.process()
    return inner
