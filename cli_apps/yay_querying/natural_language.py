"""
This module exists to solve the problem that we insert
all the Arch system files on the database, which are a
lot, and it's not possible to choose tags for all the
packages. It was needed to find an automatic solution.
We use the NLTK library to define the most used words
in the package's presentation, and use them as tags.
"""
import os

import nltk
import snoop
from loguru import logger
from mysql.connector import Error, connect


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])


@snoop
def natural_language():
    """
    We use the text on the 'package_files' files, as the
    basis to define our tags. Most of the punctuation is
    discarded as are words with less than 4 letters. We
    create a frequency map of words on each file, taking
    care to withdraw from consideration, words that are
    often repeated, but of little use; such as 'none' and
    'KiB'. We join the package name and the two most
    frequent words in a tuple that has all information for
    uploading to the database.
    https://tinyurl.com/yxwvmpa6
    """

    files = os.listdir("package_files")

    for file in files:
        if file.endswith("txt"):
            with open(f"package_files/{file}", "r") as f:
                files = f.readlines()
                fi = [i.strip() for i in files]
                fil = str(fi)  # needed as nltk accepts only strings.
                badchars = ".!?,'\":<>"
                words = [
                    word.strip(badchars)
                    for word in fil.strip().split()
                    if len(word) > 4
                ]
                word_freq = {}
                for word in words:
                    word_freq[word] = word_freq.get(word, 0) + 1
                tx = [(v, k) for (k, v) in word_freq.items()]
                tx.sort(reverse=True)
                word_freq_sorted = [(k, v) for (v, k) in tx]

                new_freq = [
                    i for i in word_freq_sorted if i[0] != "None"
                ]  # Shedding some of the words that are frequent but uninformative.
                nnew_freq = [i for i in new_freq if i[0] != "KiB"]
                nnnew_freq = [i for i in nnew_freq if i[0] != "MiB"]

                tags = []
                tag_id = []
                tags.append(
                    nnnew_freq[0][0]
                )  # We use the two most frequent words as tags.
                tags.append(nnnew_freq[1][0])
                tag_id.append((f"{file}", tags))

                try:
                    conn = connect(
                        host="localhost",
                        user="mic",
                        password="xxxx",
                        database="cli_apps",
                    )
                    cur = conn.cursor()
                    nam = tag_id[0][0][:-4]
                    tags = " ".join(map(str, tag_id[0][1]))
                    answers = [tags, nam]
                    query = "UPDATE cli_apps SET tag = %s WHERE name = %s"
                    cur.execute(query, answers)
                    conn.commit()
                except Error as e:
                    err_msg = "Error while connecting to db", e
                    print("Error while connecting to db", e)
                    if err_msg:
                        return query, e
                finally:
                    if conn:
                        conn.close()
                    
                    return query


if __name__ == "__main__":
    natural_language()
