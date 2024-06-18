# Ну, погоди! Кофейня - Telegram Bot

## Описание

Это Telegram-бот для кофейни "Ну, погоди!". Он предоставляет веб-интерфейс для сотрудников, где они могут пройти верификацию и получить доступ к различным разделам, таким как смены, места работы на карте, технологические карты, меню, новости и чат обучения.

## Установка

1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com/yourusername/telegram-web-app-bot-example.git
    cd telegram-web-app-bot-example
    ```

2. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```

3. Создайте файл `.env` и добавьте ваш Telegram Bot Token:
    ```env
    TOKEN=YOUR_TELEGRAM_BOT_TOKEN
    ```

4. Запустите бота:
    ```bash
    python bot.py
    ```

5. Разверните веб-приложение на GitHub Pages, следуя инструкциям в разделе `Quick setup` файла `README.md`.

## Быстрый запуск

1. Хостинг веб-приложения на GitHub Pages:
    - Создайте репозиторий (или форкните этот)
    - В репозитории: Settings > Pages:
        - Source: Deploy from a branch
        - Branch: main, / (root), Save
    - Подождите несколько минут для развертывания веб-приложения. Оно будет доступно по адресу: `https://<ваш_имя_пользователя>.github.io/<имя_репозитория>/index.html`

## Лицензия

Этот проект лицензирован по лицензии MIT.
