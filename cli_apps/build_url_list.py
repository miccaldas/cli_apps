"""Where we build the urls that we'll search in scrapy."""
import subprocess

import isort  # noqa: F401
import snoop
from loguru import logger

fmt = "{time} - {name} - {level} - {message}"
logger.add("../logs/info.log", level="INFO", format=fmt, backtrace=True, diagnose=True)  # noqa: E501
logger.add("../logs/error.log", level="ERROR", format=fmt, backtrace=True, diagnose=True)  # noqa: E501

subprocess.run(["isort", __file__])


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])


@logger.catch
@snoop
def build_url_list():
    """
    We get the usual structure of pypi site,
    and insert the names in the name list
    where the names usually go in the url.
    """

    with open("lists/existing.txt", "r") as f:
        names = f.readlines()

    urls = []
    for name in names:
        lname = name.lower()
        sname = lname.strip()
        url = f"https://pypi.org/project/{sname}/"
        urls.append(url)

    for url in urls:
        with open("lists/urls.txt", "a") as f:
            f.write(url)
            f.write("\n")


if __name__ == "__main__":
    build_url_list()
