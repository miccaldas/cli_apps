#!/usr/bin/env sh

######################################################################
# @author      : mclds (mclds@protonmail.com)
# @file        : upload_file_scripts
# @created     : Tuesday Feb 22, 2022 17:50:01 WET
#
# @description : Support scripts to the upload.py file. Needed
#                there are spurious '[]' in the file.
######################################################################


sed -re "s/ \[' / /g" final_text.txt > ap1.txt
sed -re "s/\]']/\]/g" ap1.txt > ap2.txt
