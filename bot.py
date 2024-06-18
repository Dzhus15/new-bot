import os
from telegram import Update, Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler
from dotenv import load_dotenv

# Загрузка переменных окружения из .env файла
load_dotenv()

TOKEN = os.getenv('TOKEN')

# Верификационные коды и данные сотрудников
EMPLOYEE_DATA = {
    'exampleCode': {
        'name': 'Иван Иванов',
        'position': 'Бариста',
        'location': 'Кофейня №1',
        'access': 'Полный'
    },
    # Добавьте больше данных сотрудников здесь
}

def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        'Добро пожаловать в кофейню "Ну, погоди!" Введите свой верификационный код:'
    )

def verify(update: Update, context: CallbackContext):
    code = update.message.text
    if code in EMPLOYEE_DATA:
        data = EMPLOYEE_DATA[code]
        reply_text = (
            f"Имя: {data['name']}\n"
            f"Должность: {data['position']}\n"
            f"Место работы: {data['location']}\n"
            f"Уровень доступа: {data['access']}\n"
        )
        keyboard = [
            [InlineKeyboardButton("Смены", callback_data='shifts')],
            [InlineKeyboardButton("Места работы на карте", callback_data='map')],
            [InlineKeyboardButton("Технологические карты", callback_data='tech-cards')],
            [InlineKeyboardButton("Меню", callback_data='menu')],
            [InlineKeyboardButton("Новости", callback_data='news')],
            [InlineKeyboardButton("Чат обучения", callback_data='training-chat')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text(reply_text, reply_markup=reply_markup)
    else:
        update.message.reply_text('Неверный верификационный код. Пожалуйста, попробуйте еще раз.')

def button(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    section_texts = {
        'shifts': 'Информация о сменах',
        'map': 'Места работы на карте',
        'tech-cards': 'Технологические карты',
        'menu': 'Меню',
        'news': 'Новости',
        'training-chat': 'Чат обучения'
    }

    query.edit_message_text(text=section_texts.get(query.data, 'Неизвестный раздел'))

def main():
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, verify))
    dp.add_handler(CallbackQueryHandler(button))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
