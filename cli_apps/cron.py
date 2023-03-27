"""Creates cron notification saying that pip update was ran."""
#import snoop
from crontab import CronTab


#def type_watch(source, value):
 #   return "type({})".format(source), type(value)


#snoop.install(watch_extras=[type_watch])


#@snoop
def cron():
    """We'll use dunst for the notification."""

    cron = CronTab("mic")
    dunst = "/usr/bin/dunstify"
    job = cron.new(command=f'{dunst} "cli_apps pip has updated."')
    job.minute.every(59)
    cron.write()


if __name__ == "__main__":
    cron()
