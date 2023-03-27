"""
We'll empty the 'package_files' and 'results' folders,
as well as the yay list.
"""
import os

#import snoop


# def type_watch(source, value):
#     return "type({})".format(source), type(value)


# snoop.install(watch_extras=[type_watch])


# @snoop
def delete_transient_files():
    """
    We'll use os.listdir to empty the
    folders, and simply delete the yay
    list.
    """

    dirs = ["package_files", "results"]
    for dir in dirs:
        for f in os.listdir(dir):
            os.remove(os.path.join(dir, f))

    os.remove("yay_lst.txt")


if __name__ == "__main__":
    delete_transient_files()
