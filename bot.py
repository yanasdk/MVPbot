from aiogram import Bot, Dispatcher, types
from aiogram import executor
import logging

# Настройки
API_TOKEN = '7652002226:AAHGsWpYqkM5yInsOrAAmPb4YS3CrgDg2b4'  # Замените на реальный токен
LANDING_URL = 'https://v0-build-something-zeta.vercel.app'  # Ваш URL лендинга

# Инициализация
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

# Кнопка "Open Portfolio"
portfolio_keyboard = types.InlineKeyboardMarkup()
portfolio_keyboard.add(types.InlineKeyboardButton(
    text="🚀 See 15-Minute Magic",
    web_app=types.WebAppInfo(url=LANDING_URL)
))

# Команда /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer(
        "Hey there! 👋 I'm Yana's MVP Bot.\n\n"
        "I was born in just 1 hour to prove one thing: when there's a cool project idea, "
        "I don't overthink - I build.\n\n"
        "This whole landing? Coded in 15 mins. Wrapped in a bot? Another 10. "
        "Deployed? While my coffee was still hot.\n\n"
        "Wanna see what I can build in 2 weeks with proper sleep? 😉",
        reply_markup=portfolio_keyboard
    )

# Обработка данных из WebApp
@dp.message_handler(content_types=['web_app_data'])
async def handle_web_app_data(message: types.Message):
    await message.answer(
        "Psst... The real magic? I'm just the demo. My creator can ship *real* MVPs "
        "faster than you can say 'scope creep'. Ping her → @yanasidikova"
    )

# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
