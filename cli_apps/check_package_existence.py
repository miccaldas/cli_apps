"""
This module will iterate through the names list and
check if the packages are really installed, as it
seems to me that the list represents what I
downloaded, not what I have,
"""
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
def check_package_existence():
    """"""


if __name__ == "__main__":
    check_package_existence()
