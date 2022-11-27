from telegram.ext import Updater, Filters, CommandHandler, MessageHandler
from bot_commands import *


updater = Updater('token')

updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('sum', sum_command))
updater.dispatcher.add_handler(CommandHandler('sub', sub_command))
updater.dispatcher.add_handler(CommandHandler('mul', mul_command))
updater.dispatcher.add_handler(CommandHandler('div', div_command))
updater.dispatcher.add_handler(CommandHandler('pow', pow_command))
updater.dispatcher.add_handler(CommandHandler('sqrt', sqrt_command))


updater.dispatcher.add_handler(MessageHandler(Filters.text, analyze_command))

updater.start_polling()
updater.idle()