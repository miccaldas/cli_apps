"""
Shows the contents of t1-t4 or names, if either
of their initial queries were positive.
"""
import pickle

# import snoop
from pyfzf.pyfzf import FzfPrompt

# from snoop import pp


# def type_watch(source, value):
#     return f"type({source})", type(value)


# snoop.install(watch_extras=[type_watch])


# @snoop
def show_column(in_binary, fzftitle, out_binary):
    """
    With the columns content from 'column_content',
    we format them with 'rich' and present them.
    """
    with open(f"{in_binary}", "rb") as f:
        lst = pickle.load(f)

    fzf = FzfPrompt()
    newcont = fzf.prompt(
        lst,
        f'--border bold --border-label="╢{fzftitle}╟" --border-label-pos bottom',
    )
    if newcont != []:
        with open(f"{out_binary}", "wb") as f:
            pickle.dump(newcont, f)


if __name__ == "__main__":
    show_column()
