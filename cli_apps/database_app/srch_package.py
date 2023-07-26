"""
Module Docstring
"""
# from configs.config import Efs, tput_config
import os
import subprocess

# import snoop
from dotenv import load_dotenv
from snoop import pp


def type_watch(source, value):
    return f"type({source})", type(value)


# snoop.install(watch_extras=[type_watch])

# load_dotenv()


# @snoop
def srch_package():
    """
    Searches for a package, regardless
    of what is in 'allinfo'. Downloads
    it to 'data_files'.
    """
    srch = input("What package do you want to look for? ")
    if srch != "":
        # First try to look for 'yay' packages by name alone...
        cmd = f"yay -Qi {srch} > data_files/{srch}_yay"
        subprocess.run(cmd, shell=True)
        # As the error the comand generates is a shell command, python
        # has no notion of an error. So, to check if the 'yay' command
        # ended successfully, we'll look at the size of supposdly created
        # file. If it's 0, it means that it errored out.
        stat = os.stat(f"data_files/{srch}_yay")
        if stat.st_size == 0:
            # If it errored out, try with a 'python-' prefix.
            cmd1 = f"yay -Qi python-{srch} > data_files/{srch}_yay"
            subprocess.run(cmd1, shell=True)
        cmd2 = f"pip show {srch} > data_files/{srch}_pip"
        subprocess.run(cmd2, shell=True)


if __name__ == "__main__":
    srch_package()
