#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Command-line interface.
"""
import click
from census_data_downloader import DOWNLOADERS

DOWNLOADERS_LOOKUP = dict((k.PROCESSED_TABLE_NAME, k) for k in DOWNLOADERS)


@click.group(help="Download Census data and reformat it for humans")
@click.argument(
    "table",
    nargs=1,
    required=True
)
@click.option(
    "--data-dir",
    nargs=1,
    default="./",
    help="The folder where you want to download the data"
)
@click.pass_context
def cmd(ctx, table, data_dir="./"):
    ctx.ensure_object(dict)
    ctx.obj['table'] = table
    ctx.obj['data_dir'] = data_dir
    try:
        klass = DOWNLOADERS_LOOKUP[ctx.obj['table']]
        ctx.obj['klass'] = klass
        ctx.obj['runner'] = klass(data_dir=data_dir)
    except KeyError:
        click.ClickException("Table not found")


@cmd.command(help="Download nationwide data")
@click.pass_context
def nationwide(ctx):
    click.echo("Hello")
    ctx.obj['runner'].download_nationwide()


@cmd.command(help="Download data for all states")
@click.pass_context
def states(ctx):
    ctx.obj['runner'].download_states()


@cmd.command(help="Download data for all Congressional districts")
@click.pass_context
def congressionaldistricts(ctx):
    ctx.obj['runner'].download_congressional_districts()


@cmd.command(help="Download data for all counties in all states")
@click.pass_context
def counties(ctx):
    ctx.obj['runner'].download_counties()


@cmd.command(help="Download data for all Census designated places")
@click.pass_context
def places(ctx):
    ctx.obj['runner'].download_places()


@cmd.command(help="Download data for all Census tracts in the provided state")
@click.argument(
    "state",
    nargs=1,
    required=True
)
@click.pass_context
def tracts(ctx, state):
    ctx.obj['runner'].download_tracts(state)


@cmd.command(help="Download data for legislative districts in the provided state")
@click.argument(
    "statelegislativedistricts",
    nargs=1,
    required=True
)
@click.pass_context
def tracts(ctx, state):
    ctx.obj['runner'].download_state_legislative_districts_upper(state)
    ctx.obj['runner'].download_state_legislative_districts_lower(state)


@cmd.command(help="Download all datasets that provide full coverage for the entire country")
@click.pass_context
def usa(ctx):
    ctx.obj['runner'].download_usa()


@cmd.command(help="Download 'em all")
@click.pass_context
def everything(ctx):
    ctx.obj['runner'].download_everything()


if __name__ == '__main__':
    cmd()
