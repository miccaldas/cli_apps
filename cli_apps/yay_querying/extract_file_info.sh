#!/usr/bin/env bash

######################################################################
# @author      : mclds (mclds@protonmail.com)
# @file        : clean_csv_files
# @created     : Sunday Feb 20, 2022 02:17:42 WET
#
# @description : As is incomparably easier to do changes to text in
#                shell than in python, I'll use this file to keep all
#                scripts I'll need to clean the original csv files.
######################################################################

results=/home/mic/python/cli_apps/cli_apps/yat_querying/results/*
texts=/home/mic/python/cli_apps/cli_apps/yay_querying/package_files/*

for file in ${texts}; do
    echo "$file"
    trunc_file=${file:61:-4}
    echo "$trunc_file"
    : '
    ftrans0="${results}${trunc_file}"
    echo "$ftrans"
    '
    # 1 - Write to file name, description and url..
    sed -nre 's/Description     : (.*$)/\1/p' "$file"
    sed -nre 's/URL             : (.*$)/\1/p' "$file"
    sed -nre 's/Name            : (.*$)/\1/p' "$file"

done
