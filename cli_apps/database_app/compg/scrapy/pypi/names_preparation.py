"""
Module to prepare the file that'll house
all information entries to use on the
Scrapy project.
"""
import pickle

# import snoop
# from snoop import pp

# def type_watch(source, value):
#     return f"type({source})", type(value)


# snoop.install(watch_extras=[type_watch])


# @snoop()
def names_preparation_scrapy():
    """
    We'll use the names in the 'names.bin'
    produced by 'link_analysis' and:
    1 - Delete repeats,
    2 - Take out slashes and points and
        replace them with underscores.
    """
    with open("finalized.bin", "rb") as f:
        final = pickle.load(f)

    # Scrapy's spider's can not have slashes or pucntuation marks
    # in them. We take them out here.
    noslashes = [(i[0], i[0].replace("-", "_"), i[1]) for i in final]
    nodots = [(i[0], i[1].replace(".", "_"), i[2]) for i in noslashes]
    spiders = [(i[0], f"{i[1]}_spider", i[2]) for i in nodots]

    with open("spiders.bin", "wb") as f:
        pickle.dump(spiders, f)


if __name__ == "__main__":
    names_preparation_scrapy()
