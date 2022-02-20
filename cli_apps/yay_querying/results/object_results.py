"""
We'll get the results information from the file, and
prepare it to be able to be uploaded to the db.
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
def organize_results():
    """
    Where we'll use the last function to
    organize our text output.
    """

    with open("res3.txt", "r") as f:
        data = f.readlines()

    clean_data = [i.strip() for i in data]
    print(clean_data)

    upld_lst = []
    batch_size = 3
    for i in range(0, len(clean_data), batch_size):
        package = clean_data[i : i + batch_size]  # noqa: E203
        upld_lst.append(package)
    print(upld_lst)

    return upld_lst


if __name__ == "__main__":
    organize_results()


@logger.catch
@snoop
def upload():
    """
    Where we uupload the content
    to the db.
    """

    lst = organize_results()

    for i in lst:
        name = i[2]
        url = i[1]
        presentation = i[0]
        answers = [name, presentation, url]
        try:
            conn = connect(host="localhost", user="mic", password="xxxx", database="cli_apps")
            cur = conn.cursor()
            query = """ INSERT INTO cli_apps (name, presentation, url) VALUES (%s, %s, %s) """
            cur.execute(query, answers)
            conn.commit()
        except Error as e:
            print("Error while connecting to db", e)
        finally:
            if conn:
                conn.close()


if __name__ == "__main__":
    upload()
