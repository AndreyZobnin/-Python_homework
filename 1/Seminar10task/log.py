from telegram import Update
from telegram.ext import CallbackContext
from datetime import datetime as dt


def log(update: Update, context: CallbackContext, text):
    time = dt.now().strftime('%d-%m-%Y %H:%M')
    file = open('D:\\Learning\\Practice\\Python\\Home_task10\\db.csv', 'a', encoding="UTF-8")
    file.write(f'{time}, {update.effective_user.first_name}, {update.effective_user.id}, {text}\n')
    file.close()