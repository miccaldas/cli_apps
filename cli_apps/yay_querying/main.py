"""
This module will call the 'tasks'
function that is decorated with
'@app.tasks()'.
"""

from app import app
from tasks import run

if __name__ == "__main__":
    run.delay()
