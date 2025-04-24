from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import logging

# Настройки
API_TOKEN = '7652002226:AAHGsWpYqkM5yInsOrAAmPb4YS3CrgDg2b4'  # Замените на реальный токен
LANDING_URL = 'https://v0-build-something-zeta.vercel.app'  # Ваш URL лендинга

# Инициализация
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

# Кнопка "Открыть портфолио"
portfolio_keyboard = types.InlineKeyboardMarkup()
portfolio_keyboard.add(types.InlineKeyboardButton(
    text="📁 Открыть моё портфолио",
    web_app=types.WebAppInfo(url=LANDING_URL)
))

# Команда /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer(
        "Привет! Я бот-портфолио Яны Сидиковой. Был сделан за 15 минут :)\n\n"
        "Нажмите кнопку ниже, чтобы увидеть примеры работ 👇",
        reply_markup=portfolio_keyboard
    )

# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
