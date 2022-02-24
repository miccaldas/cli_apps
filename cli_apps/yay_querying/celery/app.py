"""
Instantiates a Celery object, define the
backend for worker information, database,
and tells it to include the main.py file
as the module to launch, when called.
"""
from celery import Celery
from celery.schedules import crontab
from redisbeat import RedBeatSchedulerEntry, interval

app = Celery(
    "celery",
    backend="redis://localhost:6379/0",
    broker="redis://localhost:6379/0",
    include=["main"],
    interval=crontab(day_of_week=3),
    entry=RedBeatSchedulerEntry("yay_cron", "tasks.run", interval, app="celery"),
)

if __name__ == "__main__":
    app.start()
