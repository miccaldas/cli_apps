"""
This modules probes the packages that depend on given package.
A lot of times I don't don't know if a dependecy is a live
event or a fossil of a bygone era. This will help bring clarity
to these questions. This won't be so directed to immediate
consumption, we created a directory to house the data, that the
user can check any time. It'll be a more mediated experience.
"""
import os

import snoop

# import subprocess
from dotenv import load_dotenv
from snoop import pp


def type_watch(source, value):
    return f"type({source})", type(value)


snoop.install(watch_extras=[type_watch])


@snoop
def required_by(fullcont):
    """"""
    deps = []
    for line in fullcont:
        if line.startswith("Required By     :"):
            packs = line[18:]
            if " " in packs:
                lst_packs = packs.split()
                deps += lst_packs
            else:
                deps.append(packs)

    print(deps)


if __name__ == "__main__":
    required_by()
