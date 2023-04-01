"""
We'll read the 'results' files, and send their content to the db.
"""
import os
import subprocess
#import snoop

from mysql.connector import Error, connect



# def type_watch(source, value):
    # return "type({})".format(source), type(value)


# snoop.install(watch_extras=[type_watch])


# @snoop
def db_upload():
    """
    The database was previously created.
    So its just the case of iterating
    through the content lists and send
    them to the db.
    """

    folders = "/home/mic/python/cli_apps/cli_apps/yay_querying/results/"
    paths = [os.path.join(folders, file) for file in os.listdir(folders)]

    for file in paths:
        with open(file, "r") as f:
            dat = f.readlines()
            data = [i.strip() for i in dat]
            if data != []:
                name = data[2]
                presentation = data[0]
                url = data[1]
                answers = [name, presentation, url]
                try:
                    conn = connect(
                        host="localhost",
                        user="mic",
                        password="xxxx",
                        database="cli_apps",
                    )
                    cur = conn.cursor()
                    query = "INSERT INTO cli_apps (name, presentation, url) VALUES (%s, %s, %s)"
                    cur.execute(query, answers)
                    conn.commit()
                except Error as e:
                    err_msg = "Error while connection to db", e
                    print("Error while connecting to db", e)
                    if err_msg:
                        return query, e
                finally:
                    if conn:
                        conn.close()
                    
                    return query


if __name__ == "__main__":
    db_upload()
