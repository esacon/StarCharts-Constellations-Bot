# Icons made by "http://www.freepik.com/"

from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
from config import TOKEN
import bot


def main():

    updater = Updater(TOKEN, use_context=True)  # Insertar Token del bot
    dispatcher = updater.dispatcher

    # Controla el menú de opciones
    dispatcher.add_handler(CommandHandler('start', bot.start))
    dispatcher.add_handler(CommandHandler('menu', bot.menu))
    dispatcher.add_handler(CallbackQueryHandler(bot.menubutton, pattern="m1"))
    dispatcher.add_handler(CallbackQueryHandler(bot.menubutton, pattern="m2"))
    dispatcher.add_handler(CallbackQueryHandler(bot.menubutton, pattern="m3"))
    # Maneja la ayuda que provee programa para su funcionamiento
    dispatcher.add_handler(CommandHandler('help', bot.help))
    # Selecciona la imagen correspondiente
    dispatcher.add_handler(CommandHandler("constelaciones", bot.constelaciones))
    dispatcher.add_handler(CallbackQueryHandler(bot.button))
    dispatcher.add_handler(CommandHandler("stars", bot.stars))
    dispatcher.add_handler(CommandHandler("space", bot.space))
    # Lleva el control de los errores ocasionados en el programa
    dispatcher.add_error_handler(bot.error)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
