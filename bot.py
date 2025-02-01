import os
import logging
import json
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Загрузка переменных окружения
load_dotenv()

# Константы
TELEGRAM_TOKEN = "7349372655:AAFwGi3yz1sX9IS-dgTuDaeHBnpCFMbvy50"
LLM_API_URL = "http://127.0.0.1:1234/v1/chat/completions"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик команды /start"""
    await update.message.reply_text(
        "Привет! Я бот, который использует локальную модель Qwen 2.5 7B. Отправьте мне сообщение, и я отвечу вам."
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик входящих сообщений"""
    try:
        # Подготовка запроса к LLM
        payload = {
            "messages": [
                {"role": "user", "content": update.message.text}
            ],
            "model": "qwen2.5-7b-instruct-1m",
            "temperature": 0.7,
            "max_tokens": 1000
        }
        
        # Отправка запроса к локальной модели
        response = requests.post(LLM_API_URL, json=payload)
        response.raise_for_status()
        
        # Получение ответа от модели
        result = response.json()
        ai_response = result['choices'][0]['message']['content']
        
        # Отправка ответа пользователю
        await update.message.reply_text(ai_response)
        
    except Exception as e:
        logging.error(f"Ошибка при обработке сообщения: {str(e)}")
        await update.message.reply_text(
            "Извините, произошла ошибка при обработке вашего сообщения. "
            "Пожалуйста, убедитесь, что локальный LLM сервер запущен и доступен."
        )

def main():
    """Основная функция запуска бота"""
    # Создание приложения
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    # Добавление обработчиков
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Запуск бота
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main() 