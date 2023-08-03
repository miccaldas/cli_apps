"""
Main Module for Scrapy's Github module.
"""
import snoop
from dotenv import load_dotenv
from projects_creation import init_project
from snoop import pp

from db_upload import data_preparation, db_upload
from kwd_creator import kwd_creator
from names_preparation import call_analysis, names_preparation
from spider_runner import spider_runner
from epilogue import epoch_counting_info, delete_files


def type_watch(source, value):
    return f"type({source})", type(value)


snoop.install(watch_extras=[type_watch])

load_dotenv()


@snoop
def command_linux_main():
    """
    Calls all function in this folder.
    """
    call_analysis()
    res = names_preparation()
    # If call_analysis() doesn't produce results, it returns nothing.
    if res == "y":
        init_project()
        spider_runner()
        kwd_creator()
        data_preparation()
        db_upload()
        epoch_counting_info()
        delete_files()


if __name__ == "__main__":
    command_linux_main()
