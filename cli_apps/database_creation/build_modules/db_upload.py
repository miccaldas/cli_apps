"""
We'll read the last file of the transient files in
'clean_files', turn it into a list of tuples
and send it to a MySQL database.
"""
import subprocess

import isort  # noqa: F401
import snoop
from loguru import logger
from mysql.connector import Error, connect

fmt = "{time} - {name} - {level} - {message}"
logger.add("../logs/info.log", level="INFO", format=fmt, backtrace=True, diagnose=True)  # noqa: E501
logger.add("../logs/error.log", level="ERROR", format=fmt, backtrace=True, diagnose=True)  # noqa: E501

subprocess.run(["isort", __file__])


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])


@logger.catch
@snoop
def db_upload():
    """
    The database was previously created.
    So its just the case of iterating
    through the tuples, assign to each a
    to a column and the upload is
    complete.
    """

    with open("/home/mic/python/cli_apps/cli_apps/clean_files/final_text.txt", "r") as f:
        data = f.readlines()
    print(data)
    print(type(data))
    print(data[0])
    print(type(data[0]))
    print(data[0][0])
    print(type(data[0][0]))

    """for i in data:
        name = i[0]
        presentation = i[1]
        answers = [name, presentation]
        try:
            conn = connect(host="localhost", user="mic", password="xxxx", database="cli_apps")
            cur = conn.cursor()
            query = INSERT INTO cli_apps (name, presentation) VALUES (%s, %s)
            cur.execute(query, answers)
            conn.commit()
        except Error as e:
            print("Error while connecting to db", e)
        finally:
            if conn:
                conn.close()"""


if __name__ == "__main__":
    db_upload()
