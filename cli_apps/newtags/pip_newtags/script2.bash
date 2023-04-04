#!/usr/bin/env bash

###########################################################################
# @author       : mclds (mclds@protonmail.com)
# @file         : script1
# @created      : 31/03/2023
# @description  : For each file in 'urls1' folder, run sed script that
#                 deletes everything but first line and writes it to 'urls2'
#                 folder, using the same file name.
############################################################################


for FILE in urls1/*; do sed -n "1p" $FILE > urls2/$(basename $FILE); done

