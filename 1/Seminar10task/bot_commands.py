import emoji
from telegram import Update
from telegram.ext import CallbackContext
from spy_log import *

operation = 0
numbers = []

def help_command(update: Update, context: CallbackContext):

    res_str = ""
    res_str += "ПРОГРАММА КАЛЬКУЛЯТОР\n"  + emoji.emojize(":backhand_index_pointing_down:")
    res_str += "Выберите действие, затем вводите поочерёдно целые числа:\n"
    res_str += "1. Сложение /sum" + " " + emoji.emojize(":plus:")+"\n"
    res_str += "2. Вычитание /sub" + " " + emoji.emojize(":minus:")+"\n"
    res_str += "3. Умножение /mul" + " " + emoji.emojize(":multiply:")+"\n"
    res_str += "4. Деление /div" + " " + emoji.emojize(":divide:")+"\n"
    res_str += "5. Возведение в степень (первое число возвести в степень второго числа) /pow\n"
    res_str += "6. Извлечь корень (из первого числа вычислить корень степени второго числа) /sqrt\n"
    res_str += "\n"+emoji.emojize(":red_exclamation_mark:")+"Комплексное число следует вводить в одну строку через пробел, например 2 3"
    update.message.reply_text(res_str)


def sum_command(update: Update, context: CallbackContext):
    global operation
    operation = 1


def sub_command(update: Update, context: CallbackContext):
    global operation
    operation = 2


def mul_command(update: Update, context: CallbackContext):
    global operation
    operation = 3


def div_command(update: Update, context: CallbackContext):
    global operation
    operation = 4


def pow_command(update: Update, context: CallbackContext):
    global operation
    operation = 5


def sqrt_command(update: Update, context: CallbackContext):
    global operation
    operation = 6


def analyze_command(update: Update, context: CallbackContext):
    global operation, numbers
    res_str = ""

    if operation:
        if len(numbers)<2:
            msg = update.message.text
            
            if " " in msg and msg.split(" ")[0].isdigit() and msg.split(" ")[1].isdigit():
                numbers.append(complex(float(msg.split(" ")[0]), float(msg.split(" ")[1])))
                update.message.reply_text(f"Комплексное число {numbers[-1]}")
            elif msg.isdigit():
                numbers.append(float(msg))
            else:
                update.message.reply_text("Введённые данные не являются числом. Повторите ввод")
        if len(numbers) == 2:
            match operation:
                case 1:
                    res_str = f"{numbers[0]} + {numbers[1]} = {numbers[0] + numbers[1]}"
                case 2:
                    res_str = f"{numbers[0]} - {numbers[1]} = {numbers[0] - numbers[1]}"
                case 3:
                    res_str = f"{numbers[0]} * {numbers[1]} = {numbers[0] * numbers[1]}"
                case 4:
                    if numbers[1] == 0:
                        res_str = "Ошибка!"+emoji.emojize(":cross_mark:")+"Деление на ноль.\nПовторить ввод - /div"
                    else: 
                        res_str = f"{numbers[0]} / {numbers[1]} = {numbers[0] / numbers[1]}"
                case 5: 
                    res_str = f"{numbers[0]} ^ {numbers[1]} = {numbers[0] ** numbers[1]}"
                case 6: 
                    if numbers[1] == 0:
                        res_str = "Ошибка!"+emoji.emojize(":cross_mark:")+"Нет корня нулевой степени.\nПовторить ввод - /sqrt"
                    else: 
                        res_str = f"{numbers[0]} ^ (1/{numbers[1]}) = {numbers[0] ** (1 / numbers[1])}"    

            log(update, context, res_str)
            res_str += "\n\nЕщё пример? /help" + emoji.emojize(":light_bulb:")
            update.message.reply_text(res_str)
            numbers=[]
            operation=0