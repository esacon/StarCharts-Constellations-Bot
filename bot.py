"""
    Toda función que responde a los comandos del bot lleva los parámetros update y context
"""


def start(update, context):
    nombre = update.message.from_user.first_name
    update.message.reply_text("¡Hola, {}! Mi nombre es Starkbot y es un gusto ayudarte. \nPresiona /help para conocer "
                              "mis comandos \U0001F604".format(nombre))


def help(update, context):
    update.message.reply_text("Mis comandos son:\n\n\U00002734 Acércate a las estrellas con /stars\n"
                              "\n\U0001F52D Mira las constelaciones con /constelaciones\n\n\U00002728 Visualiza el "
                              "espacio completo con /starcons")


def stars(update, context):
    photo = open('photo.jpg', 'rb')
    chat_id = update.message.chat.id
    update.message.reply_text("Prepárate para ver las estella \U0001F680")
    context.bot.send_photo(chat_id=chat_id, photo=photo)


def constelaciones(update, context):
    update.message.reply_text("Prepárate conocer las constelaciones \U0001F680")


def starcons(update, context):
    update.message.reply_text("Prepárate para ver el espacio de cerca \U0001F680")
