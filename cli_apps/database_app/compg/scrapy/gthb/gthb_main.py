"""
Main Module for Scrapy's Github module.
"""
import snoop
from dotenv import load_dotenv
from projects_creation import init_project
from snoop import pp

from db_upload import data_preparation, db_upload
from kwd_creator import bin_cleaner, kwd_creator
from names_preparation import call_analysis, names_preparation
from spider_runner import spider_runner


def type_watch(source, value):
    return f"type({source})", type(value)


snoop.install(watch_extras=[type_watch])

load_dotenv()


@snoop
def gthb_main():
    """
    CAlls all function in this folder.
    """
    call_analysis()
    names_preparation()
    init_project()
    spider_runner()
    data_preparation()
    db_upload()


if __name__ == "__main__":
    gthb_main()
