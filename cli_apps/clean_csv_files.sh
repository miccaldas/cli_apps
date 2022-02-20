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

texts=/home/mic/python/cli_apps/cli_apps/text_files/*
trans=/home/mic/python/cli_apps/cli_apps/text_files/transitional_files/

for file in ${texts}; do
    read -r firstline < $file
    trunc_file=${file:46:-18}
    ftrans0="${trans}${trunc_file}trans0.txt"
    ftrans1="${trans}${trunc_file}trans1.txt"
    ftrans2="${trans}${trunc_file}trans2.txt"
    ftrans3="${trans}${trunc_file}trans3.txt"
    ftrans4="${trans}${trunc_file}trans4.txt"
    echo $ftrans0
    echo $ftrans1
    echo $ftrans2
    echo $ftrans3
    echo $ftrans4
    : '$file0=$trans/"${file}_trans0.txt"
    $file1="${file}_trans1.txt"
    $file2="${file}_trans2.txt"    
    $file3="${file}_trans3.txt"
    $file4="${file}_trans4.txt"
    # 1 - Remove the "description" lines.
    sed -re "s/description//p" "$texts"/"$file" > "$file0"
    # 2 - Remove blank lines.
    sed "/^$/d" $trans/$file_trans0.txt > $file1
    # 3 - Selects only the first occurrence of a complete phrase up to a '.'.
    sed -re "/^"$firstline"*/,/\./{p}; /\./{q}" $trans/$file_trans1.txt > $file2
    # 4 - Removes double quotes.
    sed -re s/"//g1 $trans/$file_trans2.txt > $file3
    # 5 - Removes line breaks.
    sed -z "s/\n//g" $trans/$file_trans3.txt > $filek4
    '
done
