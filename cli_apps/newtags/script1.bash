#!/usr/bin/env bash

###########################################################################
# @author       : mclds (mclds@protonmail.com)
# @file         : script1
# @created      : 31/03/2023
# @description  : For each file in 'urls' folder with 'txt' extension, run
#                 sed command that deletes a prefix 'Homepage: ' from each
#                 line. Create a file with the same name in the 'urls1'
#                 folder. 'basename' insures that we get the file name only.
#                 otherwise, $FILE would be read as 'urls/filename'
############################################################################


for FILE in urls/*.txt; do sed "s/^.*: \(http.*\)$/\1/g" $FILE > urls1/$(basename $FILE); done

