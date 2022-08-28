from aiogram import Bot, Dispatcher, executor, types
from aiogram.bot.api import TelegramAPIServer
import pytube
from pytube import *
local_server = TelegramAPIServer.from_base('http://localhost:8081')
bot = Bot(token='5339728805:AAHoSmbplCiq93adu5Bo3IX1wgR-UphokJg', server=local_server)
dp = Dispatcher(bot)

LARGE_FILE = "50 MBdan katta bo'lgan faylga path"

@dp.message_handler(content_types=['text'])
async def large_file(message: types.Message):
	yt = YouTube(link)
	# yt = yt.streams.filter(progressive=True,   file_extension='mp4').order_by('resolution').desc().first()
	yt = yt.streams.get_highest_resolution()

	a=yt.download('videos')
	videos = open(a, 'rb')

	await bot.send_video(message.chat.id, videos)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
