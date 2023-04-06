"""
Module Docstring
"""
import os
import pickle
import re
import subprocess

import snoop
from mysql.connector import Error, connect
from snoop import pp


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])


class Lists:
    """"""

    def __init__(self, cwd, lists):
        self.cwd = cwd
        self.lists = lists

    @snoop
    def yay_lst(self):
        """"""
        cmd = f"yay -Qi > {self.lists}/yay_lst.txt"
        subprocess.run(cmd, shell=True)

    @snoop
    def db_lst(self):
        """"""
        try:
            conn = connect(host="localhost", user="mic", password="xxxx", database="cli_apps")
            cur = conn.cursor()
            query = "SELECT name FROM cli_apps"
            cur.execute(query)
            recs = cur.fetchall()
        except Error as e:
            print("Error while connecting to db", e)
        finally:
            if conn:
                conn.close()

        records = [h for j in recs for h in j]
        with open(f"{self.lists}/dblst.bin", "wb") as f:
            pickle.dump(records, f)

    # @snoop
    def yay_names(self):
        """"""
        with open(f"{self.lists}/dblst.bin", "rb") as f:
            dblst = pickle.load(f)
        with open(f"{self.lists}/yay_lst.txt", "r") as v:
            yay_lst = v.readlines()

        yay_tups = []
        yaytemp = []
        for y in yay_lst:
            if y == "\n":
                yaytemp.append(y)
                yay_tups.append(yaytemp)
                yaytemp = []
            else:
                yaytemp.append(y)

        yayclean = []
        cleantemp = []
        for t in yay_tups:
            for v in t:
                if v != "\n":
                    if v.startswith("Validated By    : "):
                        nt = v.strip()
                        cleantemp.append(nt)
                        yayclean.append(cleantemp)
                        cleantemp = []
                    else:
                        cleantemp.append(v.strip())

        yayvals = [(t[0], t[2], t[4]) for t in yayclean]
        yaylst = [a[18:] for a in yayvals]
        pp(yaylst)

        # newnames = [i for i in yaylst if i not in dblst]
        # with open('newnames.bin', 'wb') as w:
        #     pickle.dump(newnames, w)


lsts = Lists(
    "/home/mic/python/cli_apps/cli_apps/yay_data",
    "/home/mic/python/cli_apps/cli_apps/yay_data/lists",
)
# lsts.yay_lst()
# lsts.db_lst()
lsts.yay_names()
