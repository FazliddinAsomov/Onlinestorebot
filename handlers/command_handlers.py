from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command


command_router= Router()


@command_router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(text="<b>Assalomu alaykum</b>")


@command_router.message(Command("help"))
async def help_handler(message: Message):
    await message.answer(text="<b>Ask from chatgpt</b>")

@command_router.message_handler(func=lambda message: True)
def search_listings(message):
    keyword = message.text.lower()
    page = 1
    per_page = 5
    while True:
        response = requests.get(f'https://api.example.com/listings?q={keyword}&page={page}&per_page={per_page}')
        data = response.json()
        listings = data.get('listings', [])
        if not listings:
            break
        for listing in listings:
            bot.send_message(message.chat.id, f"Title: {listing['title']}\nDescription: {listing['description']}")
        page += 1
bot.polling()



