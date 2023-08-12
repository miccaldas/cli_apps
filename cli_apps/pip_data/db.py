"""
MySQL module, to be shared by all modules.
"""
from typing import Any, Optional, Union

from mysql.connector import Error, connect


def dbdata(query: str, data: Any, answers: Union[list, None]) -> list:
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
        # Here because of type annotation. IT seems it doesn't like
        # or understands arguments set to 'None'. This is a workaround.
        if answers is not None:
            cur.execute(query, answers)
        else:
            cur.execute(query)
        if data == "fetch":
            data = cur.fetchall()
        if data == "commit":
            data = conn.commit()
    except Error as e:
        print("Error while connecting to db", e)
    finally:
        if conn:  # type: ignore
            conn.close()

    return data
