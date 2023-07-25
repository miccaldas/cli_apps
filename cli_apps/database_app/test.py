"""
Module Docstring
"""
import snoop

# from configs.config import Efs, tput_config
# import os
# import subprocess
from dotenv import load_dotenv
from snoop import pp

from methods import delete_empty_files, location_decision
from required_by import get_lst
from show_info import show_info


def type_watch(source, value):
    return f"type({source})", type(value)


snoop.install(watch_extras=[type_watch])

load_dotenv()


# show_info("data_files", "PACKAGES IN REQUIRED FILES")
# get_lst()
# delete_empty_files()
location_decision()
