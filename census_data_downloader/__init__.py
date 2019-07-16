#! /usr/bin/env python
# -*- coding: utf-8 -*
# flake8: NOQA
import jinja2
import logging
import pathlib
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


def inventory_everything(docs_dir):
    """
    Create markdown files describing all of the data tables.
    """
    docs_path = pathlib.Path(docs_dir)
    if not docs_path.exists():
        docs_path.mkdir()
    template_loader = jinja2.FileSystemLoader([pathlib.Path(__file__).parent.joinpath("templates")])
    template_env = jinja2.Environment(loader=template_loader)
    list_template = template_env.get_template("table_list.md")
    with open(docs_path.joinpath("TABLES.md"), 'w') as f:
        f.write(list_template.render(object_list=TABLE_LIST))


__all__ = ("TABLE_LIST", "download_everything")
