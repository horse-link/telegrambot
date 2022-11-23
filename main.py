from telegram.ext import *

print('Starting bot...')

def start_command(update, context):
    update.message.reply_text('Hello, I am a bot. You can place bets by ')


def help_command(update, context):
    update.message.reply_text('Help!')


def handle_response(text: str) -> str:
    return 'You said: ' + text


def message_handler(update, context):
    message_type = update.message.chat.type


if __name__ == '__main__':
    updater = Updater('TOKEN', use_context=True)
    dp = updater.dispatcher

    ## Commands

    ## Messages
    dp.add_handler(MessageHandler(Filters.text, message_handler))

    ## Run
    updater.start_polling(1.0)
    updater.idle()