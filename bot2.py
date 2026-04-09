import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
import time

TOKEN = "8799056389:AAHglFJ5FCvxuRC6bwGpu-oGsyJ5bv-6NgA"
ADMIN_ID = 1538410833

bot = telebot.TeleBot(TOKEN)

channels = {
    "Мой личный канал - Чихуяхуяшка": "https://t.me/LeraPriv",
    "Фото сделанные мной": "https://t.me/phootolera",
    "+ Анонимные вопросы": "https://t.me/voprosy?start=xvd4d"
}

def get_keyboard():
    keyboard = InlineKeyboardMarkup()

    for name, link in channels.items():
        keyboard.add(InlineKeyboardButton(text=name, url=link))

    return keyboard


@bot.message_handler(commands=["start"])
def start(message):
    user_id = message.from_user.id
    username = message.from_user.username if message.from_user.username else "нет username"
    name = message.from_user.first_name

    bot.send_message(
        message.chat.id,
        "Привет! Мои телеграм-каналы 👇",
        reply_markup=get_keyboard()
    )

    text = (
        f"🔥 Новый пользователь:\n"
        f"ID: {user_id}\n"
        f"Имя: {name}\n"
        f"Username: @{username}"
    )

    bot.send_message(ADMIN_ID, text)


print("Бот запущен...")

while True:
    try:
        bot.polling(none_stop=True, interval=1, timeout=20)
    except Exception as e:
        print("Ошибка:", e)
