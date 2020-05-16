# Icons made by "http://www.freepik.com/"

from telegram.ext import Updater, CommandHandler
from bot import *
from config import TOKEN


def main():
    updater = Updater(TOKEN, use_context=True)  # Insertar Token del bot
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))
    dispatcher.add_handler(CommandHandler("constelaciones", constelaciones))
    dispatcher.add_handler(CommandHandler("stars", stars))
    dispatcher.add_handler(CommandHandler("starcons", starcons))

    # dispatcher.add_error_handler(error)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()