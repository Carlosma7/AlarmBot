"""Defines an API to request trigger alarms and manage logins in the home system.

Attributes:
    app (FastAPI): FastAPI app object to define an API
"""

# pylint: disable=import-error
from fastapi import FastAPI

from src.notifications import notify_intruder, notify_login

app = FastAPI()


@app.post('/alarm')
async def alarm():
    """Notifies all habitants that the alarm has been triggered.

	Returns:
	    bool: Success state
	"""
    notify_intruder()
    return True


@app.post('/login/{access_code}')
async def login(access_code: int):
    """Checks whether an access code is logged in the system, and notifies all habitants
    that a certain user has deactivated the alarm or if its an intruder trying to do it.

	Args:
	    access_code (int): Access code of 4 digits to check if user has access to system.

	Returns:
	    bool: Success state
	"""
    notify_login(access_code)
    return True
