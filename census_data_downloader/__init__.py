#! /usr/bin/env python
# -*- coding: utf-8 -*
# flake8: NOQA
import logging
from .tables import TABLE_LIST
logger = logging.getLogger(__name__)


def download_everything(*args, **kwargs):
    """
    Download all the data.
    """
    logger.debug("Downloading all datasets for all geographies")
    for klass in TABLE_LIST:
        obj = klass(*args, **kwargs)
        logger.debug(f"Downloading {klass.PROCESSED_TABLE_NAME} dataset")
        obj.download_everything()


__all__ = ("TABLE_LIST", "download_everything")
