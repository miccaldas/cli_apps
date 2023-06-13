"""
Deletes all transient file and folders from *yay_data*.
"""
import os
import subprocess

import snoop
from snoop import pp


def type_watch(source, value):
    return f"type({source})", type(value)


snoop.install(watch_extras=[type_watch])


@snoop
def delete():
    """
    Deletes all *bin* files, keywords, lists files and the project folder.
    """

    cwd = os.getcwd()
    lists = f"{cwd}/lists"
    tags = f"{cwd}/tags"

    for c in os.listdir(cwd):
        if c.endswith(".bin"):
            os.remove(f"{cwd}/{c}")

    for lst in os.listdir(lists):
        os.remove(f"{lists}/{lst}")

    for t in os.listdir(tags):
        if t.endswith(".bin"):
            os.remove(f"{tags}/{t}")
        if t == "yay_project":
            cmd = f"/usr/bin/trash-put {tags}/{t}"
            subprocess.run(cmd, shell=True)
        if t == "kws":
            cmd1 = f"/usr/bin/trash-put {tags}/{t}/*"
            subprocess.run(cmd1, shell=True)


if __name__ == "__main__":
    delete()
