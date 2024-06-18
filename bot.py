import os
from telegram import Update, Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler
from dotenv import load_dotenv

# Загрузка переменных окружения из .env файла
load_dotenv()

# Получение токена из переменных окружения
TOKEN = os.getenv('TOKEN')

# Проверка загрузки токена
if not TOKEN:
    print("Содержимое файла .env:")
    with open('.env', 'r') as f:
        print(f.read())
    raise ValueError("Токен не найден. Пожалуйста, убедитесь, что файл .env содержит корректный токен.")

# Верификационные коды и данные сотрудников (инициализация пустого словаря)
EMPLOYEE_DATA = {}

# Обработчик команды /start
def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("Открыть веб-интерфейс", url="https://ваш-домен.github.io/ваш-репозиторий/index.html")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        'Добро пожаловать в кофейню "Ну, погоди!" Введите свой верификационный код или используйте кнопки ниже.',
        reply_markup=reply_markup
    )

# Обработчик команды для добавления верификационного кода
def add_code(update: Update, context: CallbackContext):
    if len(context.args) != 5:
        update.message.reply_text('Использование: /addcode <код> <имя> <фамилия> <должность> <место работы>')
        return
    
    code, name, surname, position, location = context.args
    EMPLOYEE_DATA[code] = {
        'name': f'{name} {surname}',
        'position': position,
        'location': location,
        'access': 'Полный'
    }
    update.message.reply_text(f'Код {code} добавлен для сотрудника {name} {surname}.')

# Обработчик для проверки верификационного кода
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

# Обработчик кнопок меню
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

# Основная функция
def main():
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("addcode", add_code))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, verify))
    dp.add_handler(CallbackQueryHandler(button))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
