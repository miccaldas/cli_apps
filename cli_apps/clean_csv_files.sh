#!/usr/bin/env sh

######################################################################
# @author      : mclds (mclds@protonmail.com)
# @file        : clean_csv_files
# @created     : Sunday Feb 20, 2022 02:17:42 WET
#
# @description : As is incomparably easier to do changes to text in
#                shell than in python, I'll use this file to keep all
#                scripts I'll need to clean the original csv files.
######################################################################


# 1 - Remove the 'description' lines.
sed -re 's/description//p' asttokens_scrapy_results.txt > ./transitional_files/asttokens_trans0.txt

# 2 - Remove blank lines.
sed "/^$/d" ./transitional_files/asttokens_trans0.txt > ./transitional_files/asttokens_trans1.txt

# 3 - Selects only the first occurrence of a complete phrase up to a '.'.
sed -re '/^The aim of the*/,/\./{p}; /\./{q}' ./transitional_files/asttokens_trans1.txt > ./transitional_files/asttokens_trans2.txt
