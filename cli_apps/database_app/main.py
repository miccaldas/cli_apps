"""
Search module that'll aggreagate several search modes, like natural search
and tag search, to broaden the scope of the information that' given.
"""
import os
import shutil
import subprocess

import click
import snoop
from snoop import pp

from location import location_main
from methods import (
    aggregate_info,
    alternative_presentations,
    checkinfo,
    delete_all_files,
    delete_empty_files,
    input_decision,
    srch_allinfo,
)
from mngmnt.ids_mngmnt import ids_mngmnt
from mngmnt.kwd_mngmnt import kwd_mngmnt
from mngmnt.names_mngmnt import names_mngmnt
from mngmnt.queries_mngmnt import queries_mngmnt
from required_by import required_main
from show_info import show_info


def type_watch(source, value):
    return f"type({source})", type(value)


snoop.install(watch_extras=[type_watch])


@click.command()
@click.argument("keywords", nargs=-1)
@click.option("-q", "--queries", multiple=True, is_flag=False, flag_value="query", default=[])
@click.option("-i", "--ids", multiple=True, is_flag=False, flag_value="id", default=[], type=int)
@click.option("-n", "--names", multiple=True, is_flag=False, flag_value="query", default=[])
@click.option("--req / --no-req", default=False)
@snoop
def get_query(keywords, queries, ids, names, req):
    """
    Because we want to deal with complex queries, we'll define that we can receive,
    in the same query, an indefinite number of keywords, queries for natural:
    language search, several id's and names. This module will receive the information
    and send output to different functions.
    """
    cwd = os.getcwd()
    data = f"{cwd}/data_files"
    required = f"{cwd}/required_files"

    keys = kwd_mngmnt(keywords)

    if queries != ():
        queries_mngmnt(queries)

    if ids != ():
        ids_mngmnt(ids)

    names_mngmnt(names)

    filelst = os.listdir(os.getcwd())
    if "qlst.bin" or "klst.bin" or "ilst.bin" or "nlst.bin" in filelst:
        checkinfo()
        aggregate_info()
        srch_allinfo()
        show_info("data_files", "PACKAGES IN DATA_FILES")
        alternative = alternative_presentations(tag="ai")
        if alternative == "required_by":
            required_main()()
        if alternative == "location_main":
            location_main("data_files")
        if alternative == ("required_by", "location_main"):
            required_main()
            location_main()
        if req:
            required_main()
            delete_empty_files()
            show_info("required_files", "PACKAGES IN REQUIRED_FILES")
            alternative_presentations(tag="req")
            if alternative == "location":
                location_main("required_files")

        delete_all_files()


if __name__ == "__main__":
    get_query()
