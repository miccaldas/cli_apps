"""
Module Docstring
"""
import snoop
from cli_apps.database_app.db import dbdata

# from configs.config import Efs, tput_config
# import os
# import subprocess
from dotenv import load_dotenv
from snoop import pp

from scrapy.kwd_creator import kwd_creator


def type_watch(source, value):
    return f"type({source})", type(value)


snoop.install(watch_extras=[type_watch])

load_dotenv()


@snoop
def test():
    """"""


if __name__ == "__main__":
    test()
