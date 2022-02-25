"""
Instantiates a Celery object, define the
backend for worker information, database,
tells it to include the main.py file
as the module to launch, when called,
and defines a periodic task to be included
on beat.
"""
from celery import Celery
from celery.schedules import crontab

app = Celery(
    "celery",
    backend="redis://localhost:6379/0",
    broker="redis://localhost:6379/0",
    include=["main"],
    beat_schedule={
        "yay_cron": {"task": "tasks.run", "schedule": crontab(day_of_week=3)},
    },
)

if __name__ == "__main__":
    app.start()
