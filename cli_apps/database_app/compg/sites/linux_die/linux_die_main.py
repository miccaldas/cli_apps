"""
Main Module of Scrapy's 'linux.die_net' project
"""
import snoop
from snoop import pp
from dotenv import load_dotenv

from names_preparation import call_analysis, names_preparation
from projects_creation import init_project
from spider_runner import spider_runner
from kwd_creator import bin_cleaner, kwd_creator
from db_upload import data_preparation, db_upload


def type_watch(source, value):
    return f"type({source})", type(value)


snoop.install(watch_extras=[type_watch])

load_dotenv()


@snoop
def linux_die_main():
    """
    We'll call all functions
    in this folder.
    """
    call_analysis()
    names_preparation()
    init_project()
    spider_runner()
    data_preparation()
    db_upload()


if __name__ == "__main__":
    linux_die_main()
