#!/usr/bin/env sh

######################################################################
# @author      : mclds (mclds@protonmail.com)
# @file        : sed_script
# @created     : Monday Feb 21, 2022 18:34:20 WET
#
# @description : These are the initial steps in the update process.
#                The first command ask pip for a list, and the second
#                isolates only the name, loosing the version.
######################################################################

pip list --format freeze > /home/mic/python/cli_apps/cli_apps/lists/pypi/first_pip.txt
sed -nre 's/(^.*)==(.*$)/\1/p' /home/mic/python/cli_apps/cli_apps/lists/pypi/first_pip.txt > /home/mic/python/cli_apps/cli_apps/lists/pypi/only_names.txt

