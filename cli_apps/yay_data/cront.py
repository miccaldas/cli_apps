"""Creates cron notification saying that yay update was ran."""
import requests
#import snoop
from crontab import CronTab


# def type_watch(source, value):
#     return "type({})".format(source), type(value)


# snoop.install(watch_extras=[type_watch])


# @snoop
def crons():
    """We'll use dunst for the notification."""

    cron = CronTab(user="mic")
    job = cron.new(command='/usr/bin/dunstify "cli_apps yay has updated."')
    job.minute.every(59)
    cron.write()

    requests.post(
        "https://ntfy.sh/mic",
        data="yay apps have been updated.".encode(encoding="utf-8"),
    )


if __name__ == "__main__":
    crons()
