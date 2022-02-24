"""
Instantiates a Celery object, define the
backend for worker information, database,
and tells it to include the main.py file
as the module to launch, when called.
"""
from celery import Celery
from celery.schedules import crontab

app = Celery(
    "celery",
    backend="redis://localhost:6379/0",
    broker="redis://localhost:6379/0",
    include=["main"],
    interval=crontab(date_of_week=3),
    entry=RedBeatSvhedulerEntry("yay_cron", "tasks.run", interval, app="celery"),
)

if __name__ == "__main__":
    app.start()
