"""
Search module that'll aggreagate several search modes, like natural search
and tag search, to broaden the scope of the information that' given.
"""
import os

import click
from dotenv import load_dotenv

from methods import (
    aggregate_info,
    checkinfo,
    delete_all_files,
    input_decision,
    loc_decision,
    req_decision,
    srch_allinfo,
)
from mngmnt.ids_mngmnt import ids_mngmnt
from mngmnt.kwd_mngmnt import kwd_mngmnt
from mngmnt.names_mngmnt import names_mngmnt
from mngmnt.queries_mngmnt import queries_mngmnt
from show_info import show_info
from use_paths import location_loop, required_loop

# import snoop
# from snoop import pp


# def type_watch(source, value):
#     return f"type({source})", type(value)


# snoop.install(watch_extras=[type_watch])
load_dotenv()


@click.command()
@click.argument("keywords", nargs=-1)
@click.option("-q", "--queries", multiple=True, is_flag=False, flag_value="query", default=[])
@click.option("-i", "--ids", multiple=True, is_flag=False, flag_value="id", default=[], type=int)
@click.option("-n", "--names", multiple=True, is_flag=False, flag_value="query", default=[])
# @snoop
def get_query(keywords, queries, ids, names):
    """
    Because we want to deal with complex queries, we'll get, in the same query, an
    indefinite number of keywords, queries for natural language search, several
    id's and names. This module will receive the information and send output to
    different functions.
    """
    da = os.getenv("DA")
    # This the mangement code block. Each option/argument, has a allocated management
    # function, that's tasked of cleaning the input and making the db calls for each
    # query. Some will ask you if you want to see a given type of data, rgardless if
    # you chose it in the command line or not. Others are more reserved.
    keys = kwd_mngmnt(keywords)
    if queries != ():
        queries_mngmnt(queries)
    if ids != ():
        ids_mngmnt(ids)
    names_mngmnt(names)

    # This is the initiation block. When you get a new query, that's what has to happen.
    filelst = os.listdir(da)
    # The names of pickled files that are created by the management modules.
    if "qlst.bin" or "klst.bin" or "ilst.bin" or "nlst.bin" in filelst:
        # Checks to see what files, from the above list, are present in the directory.
        checkinfo()
        # Joins the information in one document called 'allinfo'.
        aggregate_info()
        # Uses 'fzf' to let the user check the results and choose what he wants to see from
        # the output.
        srch_allinfo()
        # Shows a prettified version of the chosen information.
        show_info(f"{da}data_files", "PACKAGES IN DATA_FILES")
        # Two questions: do you want to see file dependencies or their location?
        re = req_decision()
        lc = loc_decision()

        # Depending on the answer, you'll be sent in a loop of functions that'll expose you
        # to the information you wanted.
        if re == "y":
            required_loop()
        if lc == "y":
            location_loop(f"{da}data_files")

    # This thing produces binary files like a motherfucker. Cleaning is in order.
    # delete_all_files()


if __name__ == "__main__":
    get_query()
