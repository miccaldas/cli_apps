from app import app
from celery import Celery
from celery.schedules import crontab
import redbeat

result_backend = "redis://localhost:6379/0"
broker_url = "redis://localhost:6379/0"
app.autodiscover_tasks(packages=["celery"])
timezone = "Europe/Lisbon"
redbeat_redis_url = "redis://localhost:6379/0"
interval = crontab(date_of_week=3)
entry = RedBeatSvhedulerEntry("yay_cron", "tasks.run", interval, app="celery")
entry.save
"""beat_schedule = {
    "yay_cron": {
        "task": "tasks.run",
        "schedule": crontab(day_of_week=3),
    }
}"""
