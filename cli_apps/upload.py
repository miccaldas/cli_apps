"""
We'll get the results information from the
'final_text.txt' file, and prepare it to be
uploaded to the db.
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
    Where we'll batch the lines 3 by 3,
    so as to have in every group: name,
    presentation, url, create a list of
    tuples and upload it to the db..
    """

    with open("/home/mic/python/cli_apps/cli_apps/clean_files/final_text.txt", "r") as f:
        data = f.readlines()

    clean_data = [i.strip() for i in data]

    upld_lst = []
    separate_lst = []
    batch_size = 3
    for i in range(0, len(clean_data), batch_size):
        package = clean_data[i : i + batch_size]  # noqa: E203
        upld_lst.append(package)
    print(upld_lst)

    for i in upld_lst:
        for d in i:
            spl = d.split(",")
            for i in spl:
                print(i)
                name = spl[0]
                presentation = spl[1:-1]
                url = spl[-1]
            separate_lst.append((name, presentation, url))

    subprocess.run("./upload_file_scripts.sh", shell=True)

    with open("ap2.txt", "r") as f:
        clean_lst = f.readlines()

    print(type(clean_lst))
    print(clean_lst[0])
    print(type(clean_lst[0]))
    print(len(clean_lst[0]))
    print(clean_lst[0][0])
    print(type(clean_lst[0][0]))
    print(clean_lst[0][0][0])
    print(type(clean_lst[0][0][0]))

    final_lst = []
    for u in clean_lst:
        print(u)
        spl1 = u.split(",")
        for y in spl1:
            print(y)
            print(spl1[0])
            print(spl1[1])
            print(spl1[2])
            print(spl1[3])
            print(spl1[4])
            """name = spl1[0]
            presentation = spl1[1:-1]
            url = spl1[-1]
            final_lst.append((name, presentation, url))
    print(final_lst)"""


if __name__ == "__main__":
    organize_results()
