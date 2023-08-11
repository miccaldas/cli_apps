"""
Clears the package of unnecessary
files. We keep 'names_linux.txt',
because it's important to compare
each draw, and only handle what is
new.
"""
import os

# import snoop


# def type_watch(source, value):
#     return "type({})".format(source), type(value)


# snoop.install(watch_extras=[type_watch])


# @snoop
def delete() -> None:
    """
    We'll delete all files in the *lists*, *kws*
    folders, and all binary and text files in
    'pip_data'.
    """
    pip = "/home/mic/python/cli_apps/cli_apps/pip_data/"
    kws = f"{pip}/kws/"
    lists = f"{pip}/lists/"

    for fld in [lists, kws]:
        if os.listdir(fld) != []:
            os.system(f"/usr/bin/trash-put {fld}/*")

    os.system(f"/usr/bin/trash-put {pip}*.bin")
    os.system(f"/usr/bin/trash-put {pip}*.txt")


if __name__ == "__main__":
    delete()


def dunst_notifier() -> None:
    """
    We'll use dunst for the notification.
    """

    os.system("/usr/bin/dunstify 'cli_apps pip has been updated.'")


if __name__ == "__main__":
    dunst_notifier()
