# Icons made by "http://www.freepik.com/"

from telegram.ext import Updater, CommandHandler
from config import TOKEN
import bot


def main():
    updater = Updater(TOKEN, use_context=True)  # Insertar Token del bot
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", bot.start))
    dispatcher.add_handler(CommandHandler("help", bot.help))
    dispatcher.add_handler(CommandHandler("constelaciones", bot.constelaciones))
    dispatcher.add_handler(CommandHandler("stars", bot.stars))
    dispatcher.add_handler(CommandHandler("starcons", bot.starcons))

    # dispatcher.add_error_handler(error)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()