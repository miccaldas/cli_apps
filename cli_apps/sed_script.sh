#!/usr/bin/env sh

######################################################################
# @author      : mclds (mclds@protonmail.com)
# @file        : sed_script
# @created     : Monday Feb 21, 2022 18:34:20 WET
#
# @description : 
######################################################################


sed -nre 's/(^.*)==(.*$)/\1/p' first_pip.txt > pip2.txt
