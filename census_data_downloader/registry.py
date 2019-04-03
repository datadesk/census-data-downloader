#! /usr/bin/env python
# -*- coding: utf-8 -*
DOWNLOADERS = []


def register_downloader(cls):
    """
    A decorator to register new classes with the application.
    """
    DOWNLOADERS.append(cls)
    return cls
