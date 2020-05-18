# Toda función que responde a los comandos del bot lleva los parámetros update y context

import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

logging.basicConfig(format='%(asctime)s - %(name)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def constelaciones(update, context):
    keyboard = [[InlineKeyboardButton("Boyero", callback_data='1'),
                 InlineKeyboardButton("Casiopea", callback_data='2')],
                [InlineKeyboardButton("Cazo", callback_data='3'),
                 InlineKeyboardButton("Cygnet", callback_data='4')],
                [InlineKeyboardButton("Geminis", callback_data='5'),
                 InlineKeyboardButton("Hydra", callback_data='6')],
                [InlineKeyboardButton("Osa Mayor", callback_data='7'),
                 InlineKeyboardButton("Osa Menor", callback_data='8')]]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Veamos las constelaciones, escoge una:', reply_markup=reply_markup)


def button(update, context):

    names = ['Boyero', 'Casiopea', 'Cazo', 'Cygnet', 'Geminis', 'Hydra', 'Osa mayor', 'Osa menor']

    const = ['Chart/Images/boyero.png', 'Chart/Images/casiopea.png', 'Chart/Images/cazo.png', 'Chart/Images/cygnet.png',
             'Chart/Images/geminis.png', 'Chart/Images/hydra.png', 'Chart/Images/osamayor.png',
             'Chart/Images/osamenor.png']

    query = update.callback_query
    query.answer()
    des = int(query.data) - 1
    query.edit_message_text(text="Ha selececcionado la constelación de {}.".format(names[des]))

    chat_id = query.message.chat_id
    photo = open(const[des], 'rb')
    query.message.reply_text("Prepárate conocer las constelaciones \U0001F680")
    query.bot.send_photo(chat_id=chat_id, photo=photo)


def start(update, context):
    nombre = update.message.from_user.first_name
    update.message.reply_text("¡Hola, {}! Mi nombre es Starkbot y es un gusto ayudarte. \nPresiona /help para conocer "
                              "mis comandos \U0001F604".format(nombre))


def help(update, context):
    update.message.reply_text("Mis comandos son:\n\n\U00002734 Acércate a las estrellas con /stars\n"
                              "\n\U0001F52D Mira las constelaciones con /constelaciones\n\n\U00002728 Visualiza el "
                              "espacio completo con /space")


def stars(update, context):
    photo = open('Chart/Images/stars.png', 'rb')
    chat_id = update.message.chat.id
    update.message.reply_text("Prepárate para ver las estella \U0001F680")
    context.bot.send_photo(chat_id=chat_id, photo=photo)


def space(update, context):
    photo = open('Chart/Images/space.png', 'rb')
    chat_id = update.message.chat.id
    update.message.reply_text("Prepárate para ver el espacio de cerca \U0001F680")
    context.bot.send_photo(chat_id=chat_id, photo=photo)


def error(update, context):
    logger.warning('La solicitud "%s" causó el error "%s"', update, context.error)
