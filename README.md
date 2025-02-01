# GB LMstudioBot

Telegram-бот для взаимодействия с локальной языковой моделью через LM Studio.

## Описание

Этот бот позволяет общаться с локальной языковой моделью Qwen 2.5 7B через Telegram интерфейс. Бот использует LM Studio для запуска модели локально.

## Требования

- Python 3.8 или выше
- LM Studio с установленной моделью qwen2.5-7b-instruct-1m
- Токен Telegram бота

## Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/ваш-username/GB-LMstudioBot.git
cd GB-LMstudioBot
```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

3. Создайте файл `.env` и добавьте в него токен вашего Telegram бота:
```
TELEGRAM_TOKEN=ваш_токен_бота
```

## Использование

1. Запустите LM Studio и активируйте модель qwen2.5-7b-instruct-1m
2. Убедитесь, что API сервер LM Studio запущен на http://127.0.0.1:1234
3. Запустите бота:
```bash
python bot.py
```
4. Найдите бота в Telegram и начните общение с ним

## Примечание

Убедитесь, что у вас достаточно мощный компьютер для запуска локальной языковой модели. 