"""
Search module that'll aggreagate several search modes, like natural search
and tag search, to broaden the scope of the information that' given.
"""
import os
import pickle
from time import sleep

import click
import snoop

# import subprocess
from mysql.connector import Error, connect
from pyfzf.pyfzf import FzfPrompt
from snoop import pp


def type_watch(source, value):
    return f"type({source})", type(value)


snoop.install(watch_extras=[type_watch])

fzf = FzfPrompt()


def dbdata(query, data):
    """
    Collects list of posts on the db.
    We'll use this function as a template,
    letting the functions that call on it
    to define its structure. That being
    the query and if using .fetchall()
    or .commit()
    This permits writing just one db function
    per module.
    """
    try:
        conn = connect(
            host="localhost",
            user="mic",
            password="xxxx",
            database="cli_apps",
        )
        cur = conn.cursor()
        cur.execute(query)
        if data == "fetch":
            data = cur.fetchall()
        if data == "commit":
            data = conn.commit()
    except Error as e:
        print("Error while connecting to db", e)
    finally:
        if conn:
            conn.close()

    return data


@snoop
def kwds_query(keys):
    """"""

    qry = []
    for i in keys:
        query = f"SELECT * FROM cli_apps WHERE t1 = '{i}' OR t2 = '{i}' OR t3 = '{i}' OR t4 = '{i}'"
        qry.append(query)
    querytups = [(g, " UNION ") for g in qry]
    querylst = [h for tup in querytups for h in tup]
    querylst.pop(-1)
    query = " ".join(querylst)

    with open("kquery.bin", "wb") as f:
        pickle.dump(query, f)


@snoop
def get_kwds():
    """"""
    with open("kquery.bin", "rb") as f:
        query = pickle.load(f)

    kl = dbdata(query, "fetch")

    with open("klst.bin", "wb") as g:
        pickle.dump(kl, g)


@snoop
def dbks():
    """"""
    query = "SELECT t1 FROM cli_apps UNION SELECT t2 FROM cli_apps UNION SELECT t3 FROM cli_apps UNION SELECT t4 FROM cli_apps"
    klst = dbdata(query, "fetch")

    kslst = [a[0] for a in klst]

    return kslst


@snoop
def showks():
    """"""
    kslst = dbks()
    print("Choose the tags that interest you. If any.")
    sleep(0.5)
    newtgs = fzf.prompt(
        kslst,
        '--border bold --border-label="╢Choose Some Tags!╟" --border-label-pos bottom',
    )
    if newtgs != []:
        with open("newtgs.bin", "wb") as f:
            pickle.dump(newtgs, f)


@click.command()
@click.argument("keywords", nargs=-1)
@click.option(
    "-q", "--query", multiple=True, is_flag=False, flag_value="query", default=[]
)
@click.option(
    "-i", "--id", multiple=True, is_flag=False, flag_value="id", default=[], type=int
)
@click.option(
    "-n", "--name", multiple=True, is_flag=False, flag_value="query", default=[]
)
@snoop
def get_query(keywords, query, id, name):
    """
    Because we want to deal with complex queries, we'll define that we can receive,
    in the same query, an indefinite number of keywords, queries for natural
    language search, several id's and names. This module will receive the information
    and send output to different functions.
    """
    cwd = os.getcwd()

    if keywords:
        kwds_query(keywords)
        get_kwds()
    else:
        getks = input("Do you want to see the avaulable keywords?[y/n] ")
        if getks == "y":
            showks()
    filelst = os.listdir(cwd)
    if "newtgs.bin" in filelst:
        with open("newtgs.bin", "rb") as f:
            mewtgs = pickle.load(f)
            kwds_query(mewtgs)

    # if query != []:
    #     with open("get_query.bin", "wb") as h:
    #         pickle.dump(query, h)

    # if id != []:
    #     with open("get_id.bin", "wb") as i:
    #         pickle.dump(id, i)

    # if name != []:
    #     with open("get_name.bin", "wb") as j:
    #         pickle.dump(name, j)
    # else:
    #     with name("get_name.bin", "wb") as m:
    #         pickle.dump(name, m)


if __name__ == "__main__":
    get_query()


# see_keys = input="Do you want to see the list of keywords?[y/n]: "
# if see_keys == 'y':
#     query = """SELECT t1 from cli_pps UNION SELECT t2 FROM cli_apps UNION
#                SELECT t3 FROM cli_apps UNION SELECT t4 FROM cli_apps"""
#     keylst = dbdata(query, 'fetch')


# @snoop
# def srch_main():
#     """
#     Calls all other functions.
#     """

# if __name__ == "__main__":
#     search()
