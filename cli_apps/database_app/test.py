"""
Module Docstring
"""
import snoop

# from configs.config import Efs, tput_config
# import os
# import subprocess
from dotenv import load_dotenv
from snoop import pp


def type_watch(source, value):
    return f"type({source})", type(value)


snoop.install(watch_extras=[type_watch])

load_dotenv()


@snoop
def test(er):
    """"""
    if er == 1:
        return "yes"
    else:
        raise SystemExit


pt = test(0)
print(pt)
