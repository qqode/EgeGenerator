from aiogram import *
import sqlite3
import re
from typing import Union
from random import *
from sqlite3 import *
from fastapi import FastAPI
from math import *
from fastapi.middleware.cors import CORSMiddleware
from itertools import *
from aiogram.utils.markdown import hspoiler
from bs4 import BeautifulSoup
import requests


con = sqlite3.connect("tasks.db", check_same_thread=False)
cur = con.cursor()
app = FastAPI()




def get2_7():
    size1 = 2 ** randint(7, 13)
    size2 = 2 ** randint(7, 13)
    v = randint(300,500)
    ex = str(cur.execute("""SELECT q FROM fuck WHERE id=702""").fetchone()[0]).format(
        size1=size1, size2=size2, v=v)
    exec(
        (cur.execute("""SELECT a FROM fuck WHERE id=702""").fetchone()[0]).format(
            size1=size1, size2=size2, v=v
        ),
        locals(),
        globals(),
    )
    return ex,otv
def get3_7():
    color1 = randint(10,30)
    color2 = randint(1,color1)
    dpi1=randint(300,700)
    dpi2=randint(100,dpi1-100)
    sred = randint(1,100)
    ex = str(cur.execute("""SELECT q FROM fuck WHERE id=703""").fetchone()[0]).format(
        dpi1=dpi1, dpi2=dpi2, color1=color1 ,color2=color2, sred=sred
    )
    exec(
        (cur.execute("""SELECT a FROM fuck WHERE id=703""").fetchone()[0]).format(
            dpi1=dpi1, dpi2=dpi2, color1=color1, color2=color2, sred=sred
        ),
        locals(),
        globals(),
    )
    return ex, otv


def get1_10():
    book = randint(100, 300)
    string = ''
    url = f'https://ilibrary.ru/text/{book}/p.1/index.html'
    html_text = requests.get(url).content
    soup = BeautifulSoup(html_text, 'html.parser')
    rang = (str(soup.find("div", class_='bnvin'))[238:240])
    author = (str(soup.find_all("div", class_="author"))[21:-7])
    name = (str(soup.find("div", class_='title')))[24:-12]
    if rang == '':
        rang = 2
    else:
        rang = int(rang)

    for i in range(1, rang):
        url = f'https://ilibrary.ru/text/{book}/p.{i}/index.html'
        html_text = requests.get(url).content
        soup = BeautifulSoup(html_text, 'html.parser')
        string += (str(soup.find_all("span", class_="p")))
    ls = string.split(' ')
    reg = re.compile('[^a-zA-Zа-яА-Я ]')
    s = reg.sub('', string)
    d = dict()
    for i in s.split():
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    res = []
    exeption = 'abcdefghijklmoops'
    for i in d:
        if str(d[i]) not in exeption:
            res.append(str(i))
    slov = choice(res)
    slov2 = ''
    for i in slov:
        if i not in 'abcdrfghigklmnopqrstuvwzx':
            slov2 += i
    otv = d[slov]
    ex = str(
        cur.execute("""SELECT q FROM fuck WHERE id = 1001""").fetchone()[0].format(slov=slov2,  name=name,author=author))
    return ex,otv


def get1_7():
    cl = randint(2, 300)
    size1 = 2 ** randint(7, 13)
    size2 = 2 ** randint(2, 18)
    ex = str(cur.execute("""SELECT q FROM fuck WHERE id=701""").fetchone()[0]).format(
        size1=size1, size2=size2, cl=cl
    )
    exec(
        (cur.execute("""SELECT a FROM fuck WHERE id=701""").fetchone()[0]).format(
            size1=size1, size2=size2, cl=cl
        ),
        locals(),
        globals(),
    )
    return ex,otv


def get4_7():
    list1 = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
    color = choice(list1)
    size1 = randint(100, 500)
    size2 = randint(100, 500)
    ex = str(
        cur.execute("""SELECT q FROM fuck WHERE id=704""")
        .fetchone()[0]
        .format(color=color, size2=size2, size1=size1)
    )
    exec(
        (
            cur.execute("""SELECT a FROM fuck WHERE id=704""")
            .fetchone()[0]
            .format(color=color, size1=size1, size2=size2)
        ),
        locals(),
        globals(),
    )
    return ex, otv


#def get5_7():
#    speedA = randint(5, 60)
#    res = randint(2, 4)
#    cle = randint(2, 4)
#    speedB = randint(2, 5)
#    ex = str(
#        cur.execute("""SELECT q FROM fuck WHERE id = 705""")
#        .fetchone()[0]
#        .format(speedB=speedB, speedA=speedA, res=res, cle=cle)
#    )
#    exec(
#        (
#            cur.execute("""SELECT q FROM fuck WHERE id=705""")
#            .fetchone()[0]
#            .format(speedB=speedB, speedA=speedA, res=res, cle=cle)
#        ),
#        locals(),
#        globals(),
#    )
#    return ex,otv
#



def get1_11():
    slov = [
        "А",
        "Б",
        "В",
        "Г",
        "Д",
        "Е",
        "Ё",
        "Ж",
        "З",
        "И",
        "Й",
        "К",
        "Л",
        "М",
        "Н",
        "П",
        "Р",
        "С",
        "Т",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "Я",
        "Ч",
    ]

    length0 = randint(5, 10)
    chars = []
    memory=randint(400,800)
    leni = 0
    for i in range(1, length0):
        a = choice(slov)
        if a not in chars:
            leni += 1
            chars.append(choice(slov))
            chars.append(" ")
    length_sims = randint(10, 30)
    amount = randint(10, 30)
    chats = "".join(chars)
    ex = str(
        cur.execute("""SELECT q FROM fuck WHERE id = 1101""")
        .fetchone()[0]
        .format(a=length_sims, b=leni, c=chats,d=amount,e=memory)
    )
    exec(
        (
            cur.execute("""SELECT a FROM fuck WHERE id=1101""")
            .fetchone()[0]
            .format(amount=amount, memory=memory, leni=leni, length_sims=length_sims)
        ),
        locals(),
        globals(),
    )
    return ex,otv

def get2_11():
    personal_code_len = randint(10, 30)
    personal_code_alph = randint(12, 74)
    personal_code_alph_and_digits=personal_code_alph+10
    '''Каждый сотрудник предприятия получает электронный пропуск, на котором записаны личный код сотрудника, код подразделения и некоторая дополнительная информация. Личный код состоит из {a} символов, каждый из которых может быть одной из {b} допустимых заглавных букв или одной из 10 цифр. Для записи личного кода используют посимвольное кодирование, все символы кодируют одинаковым минимально возможным количеством бит. Код подразделения состоит из двух натуральных чисел, не превышающих 100, каждое из которых кодируется как двоичное число и занимает минимально возможное целое число бит. Личный код и код подразделения записываются подряд и вместе занимают минимально возможное целое число байт. Всего на пропуске хранится {c} байт данных. Сколько байт выделено для хранения дополнительных сведений об одном сотруднике? В ответе запишите только целое число - количество байт'''
    memory = randint(64, 200)
    ex = str(
        cur.execute("""SELECT q FROM fuck WHERE id = 1102""")
        .fetchone()[0]
        .format(a=personal_code_len, b=personal_code_alph , c=memory)
    )
    exec(
        (
            cur.execute("""SELECT a FROM fuck WHERE id=1102""")
            .fetchone()[0]
            .format(memory=memory,personal_code_alph_and_digits=personal_code_alph_and_digits,personal_code_len=personal_code_len)
        ),
        locals(),
        globals(),
    )

    return ex,otv


def get1_8():
    s = []
    place = randint(50, 300)
    set = []
    slov = [
        "А",
        "Б",
        "В",
        "Г",
        "Д",
        "Е",
        "Ё",
        "Ж",
        "З",
        "И",
        "Й",
        "К",
        "Л",
        "М",
        "Н",
        "П",
        "Р",
        "С",
        "Т",
        "Ж",
        "Я",
        "Ч",
    ]
    wordsize = randint(4, 6)
    setsize = randint(4, 6)
    for i in range(setsize):
        set.append(slov.pop(slov.index(choice(slov))))
    set1 = "(" + "".join(set) + ")"
    #set = sorted(set)
    perebor = product(set, repeat=int(wordsize))
    place1 =place+1
    for i in perebor:
        s.append(i)
    set_sample = s[0]
    ex = str(
        cur.execute("""SELECT q FROM fuck WHERE id = 801""")
        .fetchone()[0]
        .format(wordsize=wordsize, set1=set1, place=place1,set_sample=set_sample)
    )
    exec(
        (
            cur.execute("""SELECT a FROM fuck WHERE id=801""")
            .fetchone()[0]
            .format(s=s, place=place)
        ),
        locals(),
        globals(),
    )
    return ex,otv


def get2_8():
    setr = []
    s = []
    choose = choice(("гласной", "согласной"))
    slov = [
        "А",
        "Б",
        "В",
        "Г",
        "Д",
        "Е",
        "Ё",
        "Ж",
        "З",
        "И",
        "Й",
        "К",
        "Л",
        "М",
        "Н",
        "П",
        "Р",
        "С",
        "Т",
        "O",
        "Ж",
        "Я",
        "Ч",
    ]
    vovs = ["A", "E", "Ё", "И", "О", "Я"]
    cons = [
        "Б",
        "В",
        "Г",
        "Д",
        "Ж",
        "З",
        "Й",
        "К",
        "Л",
        "М",
        "Н",
        "П",
        "Р",
        "С",
        "Т",
        "Ж",
        "Ч",
    ]
    wordsize = randint(4, 6)
    setsize = randint(4, 6)
    for i in range(setsize):
        setr.append(slov.pop(slov.index(choice(slov))))
        perebor = product("".join(setr), repeat=int(wordsize))
        k = 0
        gl = 0
        for i in perebor:
            k += 1
            if i[0] in vovs:
                gl += 1
            s.append(i)
    if choose == "гласной":
        exec(
            ("""otv=len(set(setr) & set(vovs)) * setsize ** (wordsize - 1)"""),locals(),globals(),)

    else:
        exec(("""otv=len(set(setr) & set(cons)) * setsize ** (wordsize - 1)"""),locals(),globals(),)
    ex = str(cur.execute("""SELECT q FROM fuck WHERE id = 802""").fetchone()[0].format(wordsize=wordsize, choose=choose, setr=setr))
    return ex,otv



token = '6374911798:AAEZRhVA6mpCmN5vKKAuXu6cwamrP8Jj3I0'
bot = Bot(token=token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def begin(message: types.Message):
    await bot.send_message(message.chat.id,'Привет! Введи номер задания, которое хочешь сгенерировать.(формат / + номер задания. Пока доступны: 7,11,8,10) ')


@dp.message_handler(commands=['7'])
async def begin(message: types.Message):
    await bot.send_message(message.chat.id,choice([str(get1_7()),str(get2_7()),str(get3_7()),str(get4_7())]))

#f"Видно ||Не видно||", parse_mode='MarkdownV2'


@dp.message_handler(commands=['11'])
async def begin(message: types.Message):
    await bot.send_message(message.chat.id,choice([str(get2_11()),str(get1_11())]))


@dp.message_handler(commands=['10'])
async def begin(message: types.Message):
    await bot.send_message(message.chat.id,choice([str(get1_10())]))


@dp.message_handler(commands=['8'])
async def begin(message: types.Message):
    await bot.send_message(message.chat.id,choice([str(get1_8())]))


executor.start_polling(dp)


