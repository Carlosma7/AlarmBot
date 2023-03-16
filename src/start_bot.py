"""Creates telegram bots with token in .env file.

See module telebot for Telegram bot management.
See module dotenv for .env files management.
"""

import os
import telebot
from dotenv import load_dotenv


def start_bot():
    """Loads the Telegram bot token from .env config file and creates a bot.

	Returns:
	    Telebot: Telegram bot object
	"""
    load_dotenv(dotenv_path='.env')

    token = os.getenv('TOKEN')

    if not token:
        token = input('\nPlease enter a valid Telegram Bot Token: ')

    return telebot.TeleBot(token)
