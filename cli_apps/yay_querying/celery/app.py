"""
Instantiates a Celery object, define the
backend for worker information, database,
and tells it to include the main.py file
as the module to launch, when called.
"""
from celery import Celery, crontab

app = Celery(
    "celery",
    backend="redis://localhost:6379/0",
    broker="redis://localhost:6379/0",
    include=["main"],
)

if __name__ == "__main__":
    app.start()
