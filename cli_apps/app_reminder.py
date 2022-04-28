"""
In order to remind myself of all the cli tools at
my disposal in the computer, this module will
take a random entry from the database and pass it
to dunst.
"""
import webbrowser

from mysql.connector import Error, connect


def app_reminder():
    """
    We'll take out the information from the
    database and pass it to dunst.
    As I can't seem to be able to click om
    urls in the notifications, I opted to
    open automatically the url via python.
    The module will be activated by
    a cron job.
    """

    try:
        conn = connect(host="localhost", user="mic", password="xxxx", database="cli_apps")
        cur = conn.cursor()
        query = "SELECT name, presentation, url FROM cli_apps ORDER BY rand() LIMIT 1"
        cur.execute(query)
        records = cur.fetchall()
    except Error as e:
        print("Error while connecting to db", e)
    finally:
        if conn:
            conn.close()

    name = records[0][0]
    presentation = records[0][1]
    url = records[0][2]
    webbrowser.open_new_tab(url)


if __name__ == "__main__":
    app_reminder()
