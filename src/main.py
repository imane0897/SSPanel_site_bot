"""
A simpel Telegram Bot to check in and query data traffic in N3RO.
"""
import logging
import command_handler
from info import TOKEN
from telegram.ext import Updater
from telegram.ext import CommandHandler


# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def main():
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Register command handler
    dispatcher.add_handler(CommandHandler("start", command_handler.start))
    dispatcher.add_handler(CommandHandler("checkin", command_handler.checkin))
    dispatcher.add_handler(CommandHandler("usage", command_handler.usage))

    # Start the bot
    updater.start_polling()


if __name__ == "__main__":
    main()
