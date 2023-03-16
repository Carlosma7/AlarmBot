"""Defines a bot that manages the register system of a home alarm system.

Attributes:
    bot (Telebot): Telegram bot object
    register (Register): Class that manages registration system
"""
from register import Register
from start_bot import start_bot

bot = start_bot()

register = Register()


@bot.message_handler(commands=['start'])
def start(message):
    """Starts the conversation with the bot.

    Args:
        message (json): Contains the message that contains the command which triggers the function
    """
    bot.send_message(
        message.chat.id,
        "Hi! I'm **Alarmbot**, my purpose is to manage an easy house alarm using telegram.",
        parse_mode="Markdown")


@bot.message_handler(commands=['suscribe'])
def suscribe(message):
    """Registers an user in the alarm home system, if the user isn't already registered.

    Args:
        message (json): Contains the message that contains the command which triggers the function
    """
    success = register.add(message.chat.id, message.from_user.first_name,
                           message.from_user.username)
    if success:
        bot.send_message(message.chat.id,
                         "You joined succesfully to the house register.",
                         parse_mode="Markdown")
    else:
        bot.send_message(message.chat.id,
                         "You're already in the house register.",
                         parse_mode="Markdown")


@bot.message_handler(commands=['unsuscribe'])
def unsuscribe(message):
    """Unsuscribes the user from the alarm home system, if he has already suscribed to it.

    Args:
        message (json): Contains the message that contains the command which triggers the function
    """
    success = register.remove(message.from_user.username)
    if success:
        bot.send_message(message.chat.id,
                         "You unsuscribed succesfully from the house system.",
                         parse_mode="Markdown")
    else:
        bot.send_message(
            message.chat.id,
            "You can't unsuscribe since you're not part of the system.",
            parse_mode="Markdown")


@bot.message_handler(commands=['code'])
def get_code(message):
    """Requests the access code of a registered user and messages it.

	Args:
	    message (json): Contains the message that contains the command which triggers the function
	"""
    code = register.get_code(message.from_user.username)
    if code:
        answer = f"Your private access code is {code}. Be careful and don't share it."
    else:
        answer = "You aren't registered in the system, please register first to have a code."
    bot.send_message(message.chat.id, answer, parse_mode="Markdown")


bot.polling()
