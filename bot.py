import logging 
from telegram.ext import Updater , CommandHandler, MessageHandler, Filters

import settings

logging.basicConfig(filename='bot.log', level=logging.INFO)

def greet_user(update, contex):
    print('Вызван /start')
    update.message.reply_text('Приветствую тебя, дружочек!')


def talk_to_me (update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)

def main():
    mybot = Updater(settings.API_KEY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info('Бот стартовал')
    mybot.start_polling()
    mybot.idle()

if __name__ == '__main__':
    main()