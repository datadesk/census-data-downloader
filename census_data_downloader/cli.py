#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Command-line interface.
"""
import click
from census_data_downloader.tables import TABLE_LIST
TABLES_LOOKUP = dict((k.PROCESSED_TABLE_NAME, k) for k in TABLE_LIST)


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
@click.option(
    "--year",
    default=None,
    type=int,
    help="The years of data to download. By default it gets only the latest year. Not all data are available for every year. Submit 'all' to get every year."
)
@click.option(
    '--force',
    is_flag=True,
    help="Force the downloading of the data"
)
@click.pass_context
def cmd(ctx, table, data_dir="./", year=None, force=False):
    ctx.ensure_object(dict)
    ctx.obj['table'] = table
    ctx.obj['data_dir'] = data_dir
    ctx.obj['year'] = year
    ctx.obj['force'] = force
    try:
        klass = TABLES_LOOKUP[ctx.obj['table']]
    except KeyError:
        raise click.ClickException("Table not found")
    ctx.obj['klass'] = klass
    ctx.obj['runner'] = klass(
        data_dir=data_dir,
        years=year,
        force=force
    )


@cmd.command(help="Download nationwide data")
@click.pass_context
def nationwide(ctx):
    ctx.obj['runner'].download_nationwide()


@cmd.command(help="Download divisions")
@click.pass_context
def divisions(ctx):
    ctx.obj['runner'].download_divisions()


@cmd.command(help="Download regions")
@click.pass_context
def regions(ctx):
    ctx.obj['runner'].download_regions()


@cmd.command(help="Download states")
@click.pass_context
def states(ctx):
    ctx.obj['runner'].download_states()


@cmd.command(help="Download Congressional districts")
@click.pass_context
def congressionaldistricts(ctx):
    ctx.obj['runner'].download_congressional_districts()


@cmd.command(help="Download statehouse districts")
@click.pass_context
def statelegislativedistricts(ctx):
    ctx.obj['runner'].download_state_legislative_upper_districts()
    ctx.obj['runner'].download_state_legislative_lower_districts()


@cmd.command(help="Download counties in all states")
@click.pass_context
def counties(ctx):
    ctx.obj['runner'].download_counties()


@cmd.command(help="Download Census-designated places")
@click.pass_context
def places(ctx):
    ctx.obj['runner'].download_places()


@cmd.command(help="Download urban areas")
@click.pass_context
def urbanareas(ctx):
    ctx.obj['runner'].download_urban_areas()


@cmd.command(help="Download metropolitan statistical areas")
@click.pass_context
def msas(ctx):
    ctx.obj['runner'].download_msas()


@cmd.command(help="Download combined statistical areas")
@click.pass_context
def csas(ctx):
    ctx.obj['runner'].download_csas()


@cmd.command(help="Download public use microdata areas")
@click.pass_context
def pumas(ctx):
    ctx.obj['runner'].download_pumas()


@cmd.command(help="Download New England city and town areas")
@click.pass_context
def nectas(ctx):
    ctx.obj['runner'].download_nectas()


@cmd.command(help="Download combined New England city and town areas")
@click.pass_context
def cnectas(ctx):
    ctx.obj['runner'].download_cnectas()


@cmd.command(help="Download American Indian, Alaska Native and Native Hawaiian homelands")
@click.pass_context
def aiannhhomelands(ctx):
    ctx.obj['runner'].download_aiannh_homelands()


@cmd.command(help="Download Census tracts")
@click.pass_context
def tracts(ctx):
    ctx.obj['runner'].download_tracts()


@cmd.command(help="Download ZIP Code tabulation areas")
@click.pass_context
def zctas(ctx):
    ctx.obj['runner'].download_zctas()


@cmd.command(help="Download unified school districts")
@click.pass_context
def unifiedschooldistricts(ctx):
    ctx.obj['runner'].download_unified_school_districts()


@cmd.command(help="Download elementary school districts")
@click.pass_context
def elementaryschooldistricts(ctx):
    ctx.obj['runner'].download_elementary_school_districts()


@cmd.command(help="Download secondary school districts")
@click.pass_context
def secondaryschooldistricts(ctx):
    ctx.obj['runner'].download_secondary_school_districts()


@cmd.command(help="Download Alaska Native regional corporations")
@click.pass_context
def alaskanative(ctx):
    ctx.obj['runner'].download_alaska_native()


@cmd.command(help="Download county subdivisions")
@click.pass_context
def countysubdivision(ctx):
    ctx.obj['runner'].download_county_subdivision()


@cmd.command(help="Download everything from everywhere")
@click.pass_context
def everything(ctx):
    ctx.obj['runner'].download_everything()


if __name__ == '__main__':
    cmd()
