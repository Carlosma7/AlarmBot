"""Defines all tasks to be run by task manager and control home alarm system.
"""
from invoke import task, run

# pylint: disable=unused-argument,invalid-name

# Task to clean all cache files and outputs
@task
def clean(c):
    """Cleans all the python cache files and system logs.
    """
    print("Cleaning python cache and server outputs.")
    run("find . -maxdepth 3 -type d -name __pycache__ -exec rm -r {} +")
    run("rm api.log api.err bot.log bot.err")


# Task to execute Alarmbot
@task
def execute(c):
    """Executes the API with uvicorn and the Telegram bot with corresponding logs.
    """
    print("Starting Alarmbot...")
    run("nohup uvicorn src.api:app --port 8080 --host 0.0.0.0 > ./api.log 2> ./api.err &"
        )
    run("nohup python3 src/alarm_bot.py > ./bot.log 2> bot.err &")
    print("Alarmbot is running!")


# Task to stop Alarmbot
@task
def stop(c):
    """Kills all processes related to the home alarm system.
    """
    print("Stopping Alarmbot.")
    run("kill -9 $(ps | grep uvicorn | awk '{print $1}')")
    run("kill -9 $(ps -f | grep 'python3 src/alarm_bot.py' | awk '{print $2}')"
        )
