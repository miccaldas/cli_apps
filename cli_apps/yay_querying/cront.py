"""Creates cron notification saying that yay update was ran."""
import snoop
from crontab import CronTab
from loguru import logger

fmt = "{time} - {name} - {level} - {message}"
logger.add("../logs/info.log", level="INFO", format=fmt, backtrace=True, diagnose=True)  # noqa: E501
logger.add("../logs/error.log", level="ERROR", format=fmt, backtrace=True, diagnose=True)  # noqa: E501


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])


@logger.catch
@snoop
def crons():
    """We'll use dunst for the notification."""

    cron = CronTab(user="mic")
    job = cron.new(command='/usr/bin/dunstify "cli_apps yay has updated."')
    job.minute.every(59)
    cron.write()


if __name__ == "__main__":
    crons()
