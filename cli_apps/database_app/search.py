"""
Search module that'll aggreagate several search modes, like natural search
and tag search, to broaden the scope of the information that' given.
"""
import click
import snoop

from snoop import pp
from ids_mngmnt import ids_mngmnt
from kwd_mngmnt import kwd


def type_watch(source, value):
    return f"type({source})", type(value)


snoop.install(watch_extras=[type_watch])


@click.command()
@click.argument("keywords", nargs=-1)
@click.option("-q", "--queries", multiple=True, is_flag=False, flag_value="query", default=[])
@click.option("-i", "--ids", multiple=True, is_flag=False, flag_value="id", default=[], type=int)
@click.option("-n", "--names", multiple=True, is_flag=False, flag_value="query", default=[])
@snoop
def get_query(keywords, queries, ids, names):
    """
    Because we want to deal with complex queries, we'll define that we can receive,
    in the same query, an indefinite number of keywords, queries for natural:
    language search, several id's and names. This module will receive the information
    and send output to different functions.
    """
    kwd_mngmnt(keywords)

    if queries != []:
        query_mngmnt(queries)

    if ids != []:
        ids_mngmnt(ids)

    names_mngmnt(names)


if __name__ == "__main__":
    get_query()
