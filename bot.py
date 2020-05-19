# Toda función que responde a los comandos del bot lleva los parámetros update y context

import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

logging.basicConfig(format='%(asctime)s - %(name)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def start(update, context):
    keyboard = [[InlineKeyboardButton("\U00002734 Veamos las estrellas ", callback_data='m1')],
                [InlineKeyboardButton("\U0001F52D Observemos las constelaciones", callback_data='m2')],
                [InlineKeyboardButton("\U00002728 Conoce una constelación ", callback_data='m3')]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    nombre = update.message.from_user.first_name
    update.message.reply_text("¡Hola, {} \U0001F44B! Mi nombre es Starkbot y es un placer ayudarte.\n"
                              "Soy un bot creado para ayudarte a ver el espacio más de cerca. Escoge la función que más"
                              " te guste \U0001F604:".format(nombre), reply_markup=reply_markup)


def menu(update, context):
    keyboard = [[InlineKeyboardButton("\U00002734 Veamos las estrellas ", callback_data='m1')],
                [InlineKeyboardButton("\U0001F52D Observemos las constelaciones", callback_data='m2')],
                [InlineKeyboardButton("\U00002728 Conoce una constelación ", callback_data='m3')]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    nombre = update.message.from_user.first_name
    update.message.reply_text("A continuación se despliega el menú de opciones: ", reply_markup=reply_markup)


def menubutton(update, context):
    query = update.callback_query
    query.answer()
    des = query.data
    chat_id = query.message.chat_id
    if des == 'm1':
        stars(chat_id, query)
    elif des == 'm2':
        space(chat_id, query)
    elif des == 'm3':
        constelaciones(query)


def help(update, context):
    update.message.reply_text("Es un gusto serte de ayuda, presiona /start para desplegar el menú de opciones \U0001F604.")


def stars(chat_id, query):
    photo = open('Chart/Images/stars.png', 'rb')
    query.message.reply_text("Prepárate para ver las estella \U0001F680")
    query.bot.send_photo(chat_id=chat_id, photo=photo)


def space(chat_id, query):
    photo = open('Chart/Images/space.png', 'rb')
    query.message.reply_text("Prepárate para ver el espacio de cerca \U0001F680")
    query.bot.send_photo(chat_id=chat_id, photo=photo)


def constelaciones(query):
    keyboard = [[InlineKeyboardButton("Boyero", callback_data='1'),
                 InlineKeyboardButton("Casiopea", callback_data='2')],
                [InlineKeyboardButton("Cazo", callback_data='3'),
                 InlineKeyboardButton("Cygnet", callback_data='4')],
                [InlineKeyboardButton("Geminis", callback_data='5'),
                 InlineKeyboardButton("Hydra", callback_data='6')],
                [InlineKeyboardButton("Osa Mayor", callback_data='7'),
                 InlineKeyboardButton("Osa Menor", callback_data='8')]]

    reply_markup = InlineKeyboardMarkup(keyboard)
    query.message.reply_text('A continuación tienes una lista de constelaciones, escoge una: ', reply_markup=reply_markup)


def button(update, context):

    names = ['Boyero', 'Casiopea', 'Cazo', 'Cygnet', 'Geminis', 'Hydra', 'Osa mayor', 'Osa menor']

    const = ['Chart/Images/boyero.png', 'Chart/Images/casiopea.png', 'Chart/Images/cazo.png', 'Chart/Images/cygnet.png',
             'Chart/Images/geminis.png', 'Chart/Images/hydra.png', 'Chart/Images/osamayor.png',
             'Chart/Images/osamenor.png']

    query = update.callback_query
    query.answer()
    des = int(query.data) - 1
    query.message.reply_text(text="Prepárate conocer la constelación {} \U0001F680".format(names[des]))

    chat_id = query.message.chat_id
    photo = open(const[des], 'rb')
    query.bot.send_photo(chat_id=chat_id, photo=photo)


def error(update, context):
    logger.warning('La solicitud "%s" causó el error "%s"', update, context.error)
