"""
Module that starts a new epoch.
"""
import os
import pickle

import snoop
from dotenv import load_dotenv
from snoop import pp

from methods import choice_processing, input_decision


def type_watch(source, value):
    return f"type({source})", type(value)


snoop.install(watch_extras=[type_watch])

load_dotenv()


@snoop
def start_new_epoch():
    """
    Creates a new 'epoch.bin' file.
    """
    epoch_values = input_decision("What are the values for this new epoch?")

    if epoch_values != "":
        with open("epochvals.bin", "wb") as f:
            pickle.dump(epoch_values, f)
        # 'choice_procession deals in turning a string of numbers in a lsit of strings'
        choice_processing("epochvals.bin")
        with open("choice.bin", "rb") as g:
            vals = pickle.load(g)
        # We still have to turn them to integers.
        flst = [int(vals[0]), int(vals[1])]

        with open("epoch.bin", "wb") as h:
            pickle.dump(flst, h)

    os.remove("epochvals.bin")
    os.remove("choice.bin")

    with open("../lists/noman.bin", "rb") as h:
        nm = pickle.load(h)
    data = nm[int(vals[0]) : int(vals[1])]
    with open(f"{vals[0]}_{vals[1]}.bin", "wb") as i:
        pickle.dump(data, i)


if __name__ == "__main__":
    start_new_epoch()
