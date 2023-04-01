#!/usr/bin/env sh

######################################################################
# @author      : mclds (mclds@protonmail.com)
# @file        : yay_lst
# @created     : Sunday Apr 24, 2022 17:53:36 WEST
#
# @description : Returns list of installed packages through pacman or
#                the AUR.
######################################################################

yay -Qet | awk '{print $1}' > yay_lst.txt

