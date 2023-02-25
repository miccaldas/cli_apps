"""
We'll read the files in 'results',
turn it into a list of tuples
and send it to a MySQL database.
"""
import os
import subprocess

import snoop
from db_decorator.db_information import db_information
from mysql.connector import Error, connect


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])


@snoop
@db_information
def db_upload():
    """
    The database was previously created.
    So its just the case of iterating
    through the tuples, assign to each a
    to a column and the upload is
    complete.
    """

    folders = "/home/mic/python/cli_apps/cli_apps/results/"
    paths = [os.path.join(folders, file) for file in os.listdir(folders)]

    for file in paths:
        with open(file, "r") as f:
            fdata = f.readlines()
            name = fdata[0].strip()
            presentation = fdata[1].strip()
            url = fdata[2].strip()
            answers = [name, presentation, url]
            try:
                conn = connect(
                    host="localhost", user="mic", password="xxxx", database="cli_apps"
                )
                cur = conn.cursor()
                query = (
                    "INSERT INTO cli_apps (name, presentation, url) VALUES (%s, %s, %s)"
                )
                cur.execute(query, answers)
                conn.commit()
            except Error as e:
                err_msg = "Error while connecting to db", e
                print("Error while connecting to db", e)
                if err_msg:
                    return query, e
            finally:
                if conn:
                    conn.close()
                
                return query


if __name__ == "__main__":
    db_upload()
