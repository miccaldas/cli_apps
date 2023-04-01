#!/usr/bin/env bash

######################################################################
# @author      : mclds (mclds@protonmail.com)
# @file        : clean_csv_files
# @created     : Sunday Feb 20, 2022 02:17:42 WET
#
# @description : As is incomparably easier to do changes to text in
#                shell than in python, I'll use this file to copy the
#                'Name', 'Summary', 'Location' fields, from the files
#                resulting from running 'pip show ' and send them to a
#                file, housed in the 'results' folder, with the 'Name'
#                value as its filename.
######################################################################

results=/home/mic/python/cli_apps/cli_apps/results/
texts=/home/mic/python/cli_apps/cli_apps/package_files/*

for file in ${texts}; do
    echo "$file"
    trunc_file=${file:49:-4}
    echo "$trunc_file" 
    ftrans0="${results}${trunc_file}"
    echo "$ftrans0"
    
    # 1 - Write to file name, description and url..
    sed -nre "s/^Name: (.*$)/\1/p1" "$file" >> "$ftrans0"
    sed -nre "s/^Summary: (.*$)/\1/p1" "$file" >> "$ftrans0"
    sed -nre "s/^Location: (.*$)/\1/p1" "$file" >> "$ftrans0"

done
