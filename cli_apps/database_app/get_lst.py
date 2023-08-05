"""
Makes a list of files in 'required_files' or
'data_files' and create a list odf dependencies
for each file.
"""
import snoop
from snoop import pp
import os
import pickle
from methods import delete_all_files


def type_watch(source, value):
    return f"type({source})", type(value)


snoop.install(watch_extras=[type_watch])


def get_lst(folder):
    """
    Iterates through the files in 'folder'
    and looks for information on dependencies,
    if it finds that package has dependecies,
    it adds the package name and the dependecy
    name in a tuple and stores it in a list.
    """
    # Retrieves the information asked in the command line.
    reqs = f"{os.getcwd()}/{folder}"
    fils = os.listdir(reqs)

    lst = []
    for file in fils:
        with open(f"{reqs}/{file}", "r") as f:
            fil = f.readlines()
            for f in fil:
                # Format found in files created by 'yay -Qi'
                if f.startswith("Required By     : "):
                    if f != f.startswith("Required By     : None\n"):
                        # The title and spaces occupy 18 px, the 20 px
                        # its that value and a small margin of confort.
                        if len(f) > 20:
                            # Deletes the title from the line. We now have
                            # only the dependecies names.
                            deps = f[18:]
                            lst.append((file, deps))
                # Format found in files created by 'pip show'
                if f.startswith("Required-by: "):
                    if len(f) > 15:
                        deps = f[13:]
                        lst.append((file, deps))

    # The info comes with linebreaks, we strip them and eliminate
    # entries with only "None".
    cleanlst = [(a, i.strip()) for a, i in lst if i != "None\n"]

    # If nothing's there, it'll be mostly, for not having found dependecies.
    # We delete the files of 'data_files' and raise systemexit().
    if cleanlst == []:
        print("The chosen packages are required by none.")
        delete_all_files()
        raise SystemExit
    # If we find dependencies, we look for empty spaces in the strings we
    # collected. If there's empty spaces it's because its a list of dependecies.
    # We split the string so as to create a list.
    else:
        spltlst = []
        for tup in cleanlst:
            if ", " in tup[1]:
                nw = (tup[0], tup[1].split(", "))
                for n in nw[1]:
                    if n == "":
                        nw[1].remove(n)
                spltlst.append(nw)
            else:
                nw = (tup[0], tup[1].split(" "))
                for n in nw[1]:
                    if n == "":
                        nw[1].remove(n)
                spltlst.append(nw)

        with open("spltlst.bin", "wb") as f:
            pickle.dump(spltlst, f)


if __name__ == "__main__":
    get_lst()
