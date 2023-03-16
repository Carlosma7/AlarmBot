"""Defines notifications to alert the habitants of a break-in or login from
registered habitants.

Attributes:
    bot (Telebot): Telegram bot object
    register (Register): Class that manages registration system
"""

# pylint: disable=import-error
from src.start_bot import start_bot
from src.register import Register

bot = start_bot()

register = Register()


def notify_intruder():
    """Notifies all habitants that the alarm has been triggered.
	"""
    notifications = register.get()
    for notification in notifications:
        bot.send_message(
            notification[0],
            f"Hi {notification[1]}, an intruder has been detected in the house.",
            parse_mode="Markdown")


def notify_login(access_code: int):
    """Checks whether an access code is logged in the system, and notifies all habitants
    that a certain user has deactivated the alarm or if its an intruder trying to do it.

    Args:
        access_code (int): Access code of 4 digits to check if user has access to system.
    """
    notifications = register.get()
    user = register.login(access_code)

    if not user:
        message = "The intruder has tried to login in the system."
    else:
        message = f"User **{user}** has logged in the system and deactivated the alarm."

    for notification in notifications:
        bot.send_message(notification[0], message, parse_mode="Markdown")
