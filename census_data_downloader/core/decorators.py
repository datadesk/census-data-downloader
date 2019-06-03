#! /usr/bin/env python
# -*- coding: utf-8 -*


def downloader(func):
    """
    A decorator to download data for the class returned by the parent method.
    """
    def inner(*args, **kwargs):
        config = args[0]
        klass = func(config)
        for year in config.years_to_download:
            dl = klass(config, year)
            dl.download()
            dl.process()
    return inner
