import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, CallbackContext
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

# Обработчик команды /start
async def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("Открыть веб-интерфейс", web_app=WebAppInfo(url="https://dzhus15.github.io/Telegram-bot/index.html"))],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        'Добро пожаловать в кофейню "Ну, погоди!" Используйте кнопку ниже для открытия веб-интерфейса.',
        reply_markup=reply_markup
    )

# Основная функция
def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))

    application.run_polling()

if __name__ == '__main__':
    main()
