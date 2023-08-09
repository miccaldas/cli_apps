"""
Deletes all transient file and folders from *yay_data*.
"""
import os


# @snoop
def delete():
    """
    Deletes all *bin* files, keywords, lists files.
    """

    cwd = "/home/mic/python/cli_apps/cli_apps/yay_data/"

    os.system(f"/usr/bin/trash-put {cwd}/*.bin")
    os.system(f"/usr/bin/trash-put {cwd}/lists/*")
    os.system(f"/usr/bin/trash-put {cwd}kws/*")


if __name__ == "__main__":
    delete()
