from configparser import Error

from pytube import YouTube
import telebot
import sqlite3
import time
import os
from telebot import types


def insta(message):
    import requests

    url = "https://instagram-video-or-images-downloader.p.rapidapi.com/"

    payload = f"url={message.text}"
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": "a059583912mshe99c42a2910ca5bp1fa72ejsn3dc5ddc7cf8d",
        "X-RapidAPI-Host": "instagram-video-or-images-downloader.p.rapidapi.com"
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)
#@@###instagra downloader
if not os.path.exists('videos'):
    os.makedirs('videos')

if not os.path.exists('audios'):
    os.makedirs('audios')

bot = telebot.TeleBot("5758810114:AAFGUXRlU_he0BIR1ASRlV-3owPHPzXHt0Y")
admin = 788492584

def create(id,nick_name,first_name,vaqt):
    con=sqlite3.connect('baza.db')
    cur=con.cursor()
    cur.execute("""create table if not exists users(id number,
                                                    nick_name text,
                                                    first_name text,
                                                    vaqt text)""")
    cur.execute("select id from users")
    a=cur.fetchall()
    if (id,) not in a:
        k = 0
    else:
        k = 1
    if k == 0:
        cur.execute("""insert into users values({},"{}","{}","{}")""".format(id,nick_name,first_name,vaqt))
        con.commit()
        con.close()
@bot.message_handler(commands=['start'])
def start(message):

    adminn= message.from_user.id, message.from_user.username,message.from_user.first_name, message.from_user.last_name,time.ctime()
    con=sqlite3.connect('baza.db')
    cur=con.cursor()
    cur.execute("create table if not exists users(id integer,name text,time text)")
    cur.execute("select id from users")
    user=cur.fetchall()
    l=[]
    for i in user:
        l.append(i[0])
    if message.chat.id not in l:
      cur.execute(f"""insert into users values({message.chat.id},
                                                '{message.from_user.first_name}',
                                                '{time.localtime()[:5]}')""")
    con.commit()
    con.close()
    keyboard = types.ReplyKeyboardMarkup(row_width=6,resize_keyboard=True) #создаем клавиатуру
    webAppTest = types.WebAppInfo("https://youtube.com") #создаем webappinfo - формат хранения url
    YouTube = types.KeyboardButton(text="YouTube", web_app=webAppTest) #создаем кнопку типа webapp
    webAppTest = types.WebAppInfo("https://tiktok.com") #создаем webappinfo - формат хранения url
    TikTok = types.KeyboardButton(text="TikTok", web_app=webAppTest) #создаем кнопку типа webapp
    keyboard.add(YouTube,TikTok) #добавляем кнопки в клавиатуру

    bot.send_message(message.chat.id, """<b>Привет, через этого бота можно скачивать видео из YouTube, Tik-Tok.
Отправьте ссылку на видео, которое хотите скачать:</b>""", reply_markup=keyboard, parse_mode='html')
    return keyboard

panel = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
a = types.KeyboardButton("📤  Xabar  yuborish")
b = types.KeyboardButton("📊  Userlar  soni")
c = types.KeyboardButton("📤  Reklama  yuborish")
d = types.KeyboardButton("📂  Malumotlar  bazasi")
e = types.KeyboardButton("👤  Userga  yuborish")
ads=types.KeyboardButton("ADS Chat")
o = types.KeyboardButton("♻️  START")
x = types.KeyboardButton("🆘  HELP")
panel.row(a, c)
panel.row(d, b)
panel.row(e,ads)
panel.row(o, x)
cancel = types.ReplyKeyboardMarkup(resize_keyboard=True)
l = types.KeyboardButton("❌  BEKOR  QILISH  ❌")
cancel.row(l)

def reklama(message):
    con=sqlite3.connect('baza.db')
    cur=con.cursor()

    cur.execute("SELECT rek FROM adse")
    starts=cur.fetchall()
    con.commit()
    con.close()
    bot.send_message(message.chat.id, starts[-1])


@bot.message_handler(content_types=['text'])
def admin_panel(message):

    con=sqlite3.connect('baza.db')
    cur=con.cursor()
    cur.execute("create table if not exists users(id integer,name text,time text)")
    cur.execute("select id from users")
    user=cur.fetchall()
    l=[]
    for i in user:
        l.append(i[0])
    if message.chat.id not in l:
      cur.execute(f"""insert into users values({message.chat.id},
                                                '{message.from_user.first_name}',
                                                '{time.localtime()[:5]}')""")
    con.commit()
    con.close()
    global link
    link = message.text
    ## -- ##  commands  ## -- ##
    if message.text == '/panel':
       bot.send_message(admin, "<b>Admin panelga hush kelipsiz !</b>", parse_mode='html', reply_markup=panel)

    elif message.text == '♻️  START':
        bot.send_message(message.chat.id, "/start - commandasini malumotlarini o'zgartirish\n\nmalumot kiriting  :", reply_markup=cancel)
        bot.register_next_step_handler(message, starts)

    elif message.text == '🆘  HELP':
        bot.send_message(message.chat.id, "/help - commandasini malumotlarini o'zgartirish\n\nmalumot kiriting  :", reply_markup=cancel)
        bot.register_next_step_handler(message, helps)

    elif message.text == '/help':
        try:
            bot.send_message(message.chat.id, helper)
        except:
            bot.send_message(message.chat.id, """Как пользоваться:
  1. Зайдите в одну из социальных сетей.
  2. Выберите интересное для вас видео.
  3. Нажми кнопку «Скопировать».
  4. Отправьте нашему боту и получите ваш файл!

Бот может скачивать с:
   1. TikTok
   2. YouTube""")


    ## -- ##  button  ## -- ##
    elif message.text=="ADS Chat":
        bot.send_message(message.chat.id,"'Text Ads Chat'ni Yuboring 🔼 ")
        bot.register_next_step_handler(message, adse)

    elif message.text == "👤  Userga  yuborish":
        bot.send_message(788492584, "<b>👤  Userni  🆔-sini  kiriting  :</b>", parse_mode='html', reply_markup=cancel)
        bot.register_next_step_handler(message, id_ga)

    elif message.text == "📂  Malumotlar  bazasi":
        bot.send_document(message.chat.id, open("baza.db", "rb"))

    elif message.text == "📤  Xabar  yuborish":
        msg = bot.send_message(admin, "<b>Knopkasiz habar yuboring  : </b>", parse_mode='html', reply_markup=cancel)
        bot.register_next_step_handler(msg, send)

    elif message.text == "📤  Reklama  yuborish":
        msg = bot.send_message(admin, "<b>Knopkali xabar yuboring  : </b>", parse_mode='html', reply_markup=cancel)
        bot.register_next_step_handler(msg, forwar)

    elif message.text == "📊  Userlar  soni":
        con=sqlite3.connect('baza.db')
        cur=con.cursor()
        cur.execute("select id from users")
        user=cur.fetchall()
        con.commit()
        con.close()
        l=[]
        for i in user:
            l.append(i[0])
        for i in l:
            a=len(l)
        try:
            bot.send_message(admin, f"<b>👥 Umumiy foydalanuvchilar soni : {a} ta\n\n✅ Aktivlar soni : {ketti} ta\n\n❌ Spam berganlar soni {ketmadi} ta</b>", parse_mode='html')
        except:
            bot.send_message(admin, f"<b>👥 Umumiy foydalanuvchilar soni : {a} ta</b>", parse_mode='html')

    elif message.text == "❌  BEKOR  QILISH  ❌":
        bot.send_message(admin, "<b>Bekor  qilindi  ❗</b>", parse_mode='html', reply_markup=panel)


    else:
        mainn(message)
#Hamma userlarga habar yuborish
def starts(message):
    global starter
    if message.text == "❌  BEKOR  QILISH  ❌":
        bot.send_message(admin, "<b>Bekor  qilindi  ❗</b>", parse_mode='html', reply_markup=panel)
    else:
        starter = message.text
        bot.send_message(message.chat.id, "/start - commadndasi muvafaqiyatli o'zgartirildi ✅", reply_markup=panel)

def helps(message):
    global helper
    if message.text == "❌  BEKOR  QILISH  ❌":
        bot.send_message(admin, "<b>Bekor  qilindi  ❗</b>", parse_mode='html', reply_markup=panel)
    else:
        helper = message.text
        bot.send_message(message.chat.id, "/help - comandasi muvafaqiyatli o'zgartirildi ✅", reply_markup=panel)
#Hamma userlarga habar yuborish
def adse(message):
    con=sqlite3.connect('baza.db')
    cur=con.cursor()
    cur.execute("create table if not exists ads(reklama text)")
    cur.execute("select  reklama from ads")
    user=cur.fetchall()
    l=[]
    for i in user:
        l.append(i[0])
    if message.chat.id not in l:
      cur.execute(f"""insert into ads values('{message.text}')""")
    con.commit()
    con.close()
def send(message):
    global ketti
    global ketmadi
    if message.text == "❌  BEKOR  QILISH  ❌":
        bot.send_message(admin,"<b>Xabarni jo'natish bekor qilindi ❗</b>", parse_mode='html', reply_markup=panel)
    else:
        boshi = time.time()
        con=sqlite3.connect('baza.db')
        cur=con.cursor()
        cur.execute("select id from users")
        user=cur.fetchall()
        con.commit()
        con.close()
        l=[]
        for i in user:
            l.append(i[0])
            print(i[0])
        ketti = 0
        ketmadi = 0
        for i in l:
            a = len(l)
        for i in l:
            try:
                bot.copy_message(i, message.chat.id, message.id)
                ketti += 1
            except:
                ketmadi += 1
        oxiri = time.time()
        bot.send_message(admin, f"<b>{a}  :  ta  foydalanuvchidan  👥\n\n{ketti}  :  tasiga  yuborildi  ✅\n\n{ketmadi}  :  tasiga  yuborilmadi  ❌\n\nXabar  {round(boshi-oxiri)} - secundda userlarga yuborildi ✅</b>", parse_mode='html', reply_markup=panel)

def forwar(message):
    global ketti
    global ketmadi
    if message.text == "❌  BEKOR  QILISH  ❌":
        bot.send_message(admin,"<b>Xabarni jo'natish bekor qilindi ❗</b>", parse_mode='html', reply_markup=panel)
    else:
        boshi = time.time()
        con=sqlite3.connect('baza.db')
        cur=con.cursor()
        cur.execute("select id from users")
        user=cur.fetchall()
        con.commit()
        con.close()
        l=[]
        for i in user:
            l.append(i[0])
            print(i[0])
        ketti = 0
        ketmadi = 0
        for i in l:
            a = len(l)
        for i in l:
            try:
                bot.forward_message(i, message.chat.id, message.id)
                ketti += 1
            except:
                ketmadi += 1
        oxiri = time.time()
        bot.send_message(admin, f"<b>{a}  :  ta  foydalanuvchidan  👥\n\n{ketti}  :  tasiga  yuborildi  ✅\n\n{ketmadi}  :  tasiga  yuborilmadi  ❌\n\nXabar  {round(boshi-oxiri)} - secundda userlarga yuborildi ✅</b>", parse_mode='html', reply_markup=panel)

#User id-siga habar yuborish
def id_ga(message):
    if message.text == "❌  BEKOR  QILISH  ❌":
        bot.send_message(admin,"<b>Xabarni jo'natish bekor qilindi ❗</b>", parse_mode='html', reply_markup=panel)
    else:
        global id_si
        id_si = message.text
        bot.send_message(788492584, "<b>Userga  yubormoqchi  bo'lgan  habaringizni  yuboring   :</b>", parse_mode='html')
        bot.register_next_step_handler(message, yub)

def yub(message):
    if message.text == "❌  BEKOR  QILISH  ❌":
        bot.send_message(admin,"<b>Xabarni jo'natish bekor qilindi ❗</b>", parse_mode='html', reply_markup=panel)
    else:
        try:
            bot.copy_message(id_si, message.chat.id, message.id)
            bot.send_message(admin, "Xabaringiz yuborildi ✅")
        except:
            bot.send_message(admin, "Xabaringiz yuborilmadi ❌")


def mainn(message):
    if message.text.startswith('http://www.tiktok.com') or message.text.startswith('http://vm.tiktok.com') or message.text.startswith('http://vt.tiktok.com') or message.text.startswith('https://www.tiktok.com') or message.text.startswith('https://vm.tiktok.com') or message.text.startswith('https://vt.tiktok.com')  or message.text.startswith('https:') or message.text.startswith('http:') or message.text.startswith('.com'):

        try:
            try:
                    try:
                        yt = YouTube(link)
                        # yt = yt.streams.filter(progressive=True,   file_extension='mp4').order_by('resolution').desc().first()
                        yt = yt.streams.get_highest_resolution()

                        a=yt.download('videos')
                        videos = open(a, 'rb')

                        bot.send_video(message.chat.id, videos, caption=f'<b>{yt.title}</b>', parse_mode='html')
                        con=sqlite3.connect('baza.db')
                        cur=con.cursor()

                        cur.execute("SELECT reklama FROM ads")
                        starts=cur.fetchall()
                        con.commit()
                        con.close()
                        bot.send_message(message.chat.id, starts[-1])

                        videos.close()
                        os.remove(a)
                    except:

                                

                            pass
            except:
                insta(message)
        except:
            pass
    else:
        pass

bot.infinity_polling()

#version 2.1
