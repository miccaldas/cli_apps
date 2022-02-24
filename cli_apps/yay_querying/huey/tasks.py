"""
Module to schedule updates of the information
collected from yay.
"""
import os
import subprocess
from datetime import datetime
from time import sleep

import isort  # noqa: F401
import snoop
from systemd import journal

from config import crontab, huey
from main import main

subprocess.run(["isort", __file__])


@huey.periodic_task(crontab(day_of_week="3"))
def update():
    """
    It will call the main function and start the
    updating process.
    """
    main()


if __name__ == "__main__":
    update()
