"""
Module that defines universal variables and defines the
paths to take inside the app.
The idea is to automate as much as reasonably possible,
The process from defining the range of apps to be analyzed
to the web search, finishing in the database upload.
"""
import os
import pickle

import snoop
from cli_apps.database_app.methods import input_decision
from cli_apps.database_app.required_by import choice_processing
from dotenv import load_dotenv
from snoop import pp

from get_information import target_definition
from scrapy.linux_die.linux_die_main import linux_die_main


def type_watch(source, value):
    return f"type({source})", type(value)


snoop.install(watch_extras=[type_watch])

load_dotenv()
# Envs
db = os.getenv("DBAPP")
comp = os.getenv("COMP")
app = os.getenv("APPDATA")


@snoop
def epoch_definition():
    """
    We'll define an interval of apps
    in indexes, that'll define the
    'epoch' where all functions work.
    Until a given 'epoch' is solved,
    there'll be no more inputs.
    Here we ask for the max and min
    values of the split the user wants
    and ceate a file that'll be consulted
    by all others, whenver information
    on this is necessary.
    """
    epoch_values = input_decision("Define the min and max values of the split.")
    with open("epoch_values.bin", "wb") as f:
        pickle.dump(epoch_values, f)

    # 'choice_processing' untangles strings with
    # lists of ints, and turns them to a list of
    # strings.
    choice_processing(f"{comp}epoch_values.bin")
    with open("choice.bin", "rb") as g:
        str_epoch = pickle.load(g)
    # We turn the list of strings to ints.
    epoch_lst = [int(i) for i in str_epoch]
    with open(f"{comp}epoch.bin", "wb") as h:
        pickle.dump(epoch_lst, h)

    os.remove("choice.bin")
    os.remove("epoch_values.bin")


@snoop
def preffered_information_calls():
    """
    We'll cycle through our preffered
    sites, and see if there's entries
    with them in our cohort, and if
    they can produce worthwile info.
    """
    epoch_definition()
    target_definition()
    linux_die_main()


@snoop
def final_data_collection():
    """
    Collects the files with the results of
    the anaylsis per site.
    """
    pass


@snoop
def data_analysis():
    """
    We'll look at the data ollected and
    determine if it's worthwhile.
    """
    pass


@snoop
def new_measures():
    """"""
    pass
