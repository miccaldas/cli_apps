"""
Module where we define the tasks
of the pip update process.
"""
import snoop

from cron import cron
from data_preparation import alternative_urls, len_check, list_conciliation, xorg_urls
from db_upld import db_upload
from delete import delete
from kwd_preparation import kwd_collector, kwd_creator
from lists import db_data, new_entries, pip_list, pip_show, txt_cleaner

# def type_watch(source, value):
#     return f"type({source})", type(value)


# snoop.install(watch_extras=[type_watch])


@snoop
def main():
    """
    We get a list of package names in the db,
    another list of packages installed by 'pip',
    If there's packages in pip's list not in the
    db, new_entries() will create a list with
    their names and return nothing. If nothing new
    was found, it'll return 'n'.
    If it doesn't return 'n', we know that we can
    continue the process.
    """

    # db_data()
    # pip_list()
    ne = new_entries()
    # if ne != "n":
    #     pip_show()
    #     txt_cleaner()
    #     alternative_urls()
    #     xorg_urls()
    #     len_check()
    #     list_conciliation()
    #     kwd_creator()
    #     kwd_collector()
    #     db_upload()
    #     cron()
    # delete()


if __name__ == "__main__":
    main()
