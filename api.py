# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from tabulate import tabulate
import sqlite3
import re
import requests
from typing import Union
from random import *
from sqlite3 import *
from fastapi import FastAPI
from math import *
from fastapi.middleware.cors import CORSMiddleware
from itertools import *

con = sqlite3.connect("tasks.db", check_same_thread=False)
cur = con.cursor()
app = FastAPI()

origins = ["http://localhost", "http://localhost:8080", "*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get1_2():
    # все работает правильно с стабильным условием, я хз как оно будет работать с генерируемым условием, но это уже работа Криюшина. Ко мне по вопросам работы этого алгоритма не оброщаться, так как я писал это не на трезвую голову ( болею) и скорее всего забуду как это работает, однако в двух словах ответ - это рандомный шафл нужных символов, дальше алгоритм генерит условие и по нему прогоняет стандартный алгоритм решения, записывая результаты в словарь data с индексами  x y z w , потом задание формируется как таблица, беря данные из словаря data, меняя ключи на переменная 1, переменная 2 и тд. В результате набор символов из ответа соответствует переменным из таблицы
    res = ''
    letters = ['x', 'y', 'z', 'w',
               '(x≡y)', '(x≡w)', '(x≡z)', '(w≡y)', '(z≡w)', '(z≡y)',
               '(x∨y)', '(x∨w)', '(x∨z)', '(w∨y)', '(z∨w)', '(z∨y)',
               '(x∧y)', '(x∧w)', '(x∧z)', '(w∧y)', '(z∧w)', '(z∧y)'
               ]
    syms = ['->', '∨', '∧', '≡']
    pow = randint(3, 5)
    while pow != 0:
        if pow > 1:
            res += choice(letters)
            res += choice(syms)
        else:
            res += choice(letters)
        pow -= 1
    for i in res:
        if '∧' in res:
            res = res.replace('∧', ' and ')
        if '∨' in res:
            res = res.replace('∨', ' or ')
        if '≡' in res:
            res = res.replace('≡', ' == ')
        if '->' in res:
            res = res.replace('->', ' <= ')
    c = randint(0, 1)
    data = {'x': [], 'y': [], 'z': [], 'w': [], 'f': []}
    otv = ['x', 'y', 'z', 'w']
    shuffle(
        otv)  # проверить, как работает при запуске в функции, если каждый раз ответ xyzw, то это баг и эта функция не работает с функцией
    for x in range(2):
        for y in range(2):
            for z in range(2):
                for w in range(2):
                    f = res
                    if eval(f) == c:
                        data['x'].append(x)
                        data['y'].append(y)
                        data['z'].append(z)
                        data['w'].append(w)
                        data['f'].append(int(eval(f)))
    tabl = []
    for i in range(len(otv)):
        tabl.append(['Переменная' + ' ' + str(i + 1), data[str(otv[i])]])
    tabl.append(['Функция', data['f']])
    ex = tabulate([tabl])
    return {"task": ex, "uid": otv}

def get1_7():
    cl = randint(2, 300)
    size1 = 2 ** randint(7, 13)
    size2 = 2 ** randint(2, 300)
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
    return {"task": ex, "uid": otv}


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
    return {"task": ex, "uid": otv}


def get3_7():
    dpi2 = randint(100, 300)
    dpi1 = randint(310, 600)
    color1 = randint(16, 24)
    color2 = randint(2, 12)
    sred = randint(10, 100)
    ex = str(
        cur.execute("""SELECT q FROM fuck WHERE id=703""")
        .fetchone()[0]
        .format(dpi1=dpi1, dpi2=dpi2, color1=color1, color2=color2, sred=sred)
    )
    exec(
        (cur.execute("""SELECT a FROM fuck WHERE id=703""").fetchone()[0]).format(
            dpi1=dpi1, dpi2=dpi2, color1=color1, color2=color2, sred=sred
        ),
        locals(),
        globals(),
    )
    return {"task": ex, "uid": otv}


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
    return {"task": ex, "uid": otv}


def get5_7():
    speedA = randint(5, 60)
    res = randint(2, 4)
    cle = randint(2, 4)
    speedB = randint(2, 5)
    ex = str(
        cur.execute("""SELECT q FROM fuck WHERE id = 705""")
        .fetchone()[0]
        .format(speedB=speedB, speedA=speedA, res=res, cle=cle)
    )
    exec(
        (
            cur.execute("""SELECT q FROM fuck WHERE id=705""")
            .fetchone()[0]
            .format(speedB=speedB, speedA=speedA, res=res, cle=cle)
        ),
        locals(),
        globals(),
    )
    return {"task": ex, "uid": otv}


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
    return {"task": ex, "uid": otv}


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

    return {"task": ex, "uid": otv}


def get1_19():
    otv = []
    adder1 = randint(1, 8)
    adder2 = randint(1, 8)
    mult = randint(2, 4)
    pit = randint(20, 99)
    ex = str(
        cur.execute("""SELECT q FROM fuck WHERE id = 1102""")
        .fetchone()[0]
        .format(adder2=adder2, adder1=adder1, mult=mult, pit=int(pit) - 1)
    )
    exec(
        (
            cur.execute("""SELECT q FROM fuck WHERE id=1102""")
            .fetchone()[0]
            .format(pit=pit, mult=mult)
        ),
        locals(),
        globals(),
    )
    return {"task": ex, "uid": otv}


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
    set = (set)
    perebor = product(set, repeat=int(wordsize))
    for i in perebor:
        s.append(i)
    ex = str(
        cur.execute("""SELECT q FROM fuck WHERE id = 801""")
        .fetchone()[0]
        .format(set1=set1, wordsize=wordsize, s=s, place=place)
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
    return {"task": ex, "uid": otv}


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
    otv = 0
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
            """otv=len(set(setr) & set(vovs)) * setsize ** (wordsize - 1)"""
        )  # переписать под sql
    else:
        exec("""otv=len(set(setr) & set(cons)) * setsize ** (wordsize - 1)""")
    ex = str(cur.execute("""SELECT q FROM fuck WHERE id = 802"""))
    return {"task": ex, "uid": otv}

#тестить
def get1_10():
 
    book = randint(100,300)
    string=''
    url = f'https://ilibrary.ru/text/{book}/p.1/index.html'
    html_text = requests.get(url).content
    soup = BeautifulSoup(html_text, 'html.parser')
    rang = (str(soup.find("div",class_='bnvin'))[238:240])
    author =(str(soup.find_all("div", class_="author"))[21:-7])
    name = (str(soup.find("div",class_='title')))[24:-12]
    if rang =='':
        rang=2
    else:
        rang=int(rang)

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
    slov2=''
    for i in slov:
        if i not in 'abcdrfghigklmnopqrstuvwzx':
            slov2+=i
    otv = d[slov]
    ex = str(cur.execute("""SELECT q FROM fuck WHERE id = 1001""").fetchone()[0].format(slov=slov2,author=author,name=name))
    return {"task": ex, "uid": otv}


@app.get("/getTask")
def getTask(task_type):
    if task_type == "1_7":
        return get1_7()
    elif task_type == '1_2':
        return get1_2()
    elif task_type == "2_7":
        return get2_7()
    elif task_type == "3_7":
        return get3_7()
    elif task_type == "4_7":
        return get4_7()
    elif task_type == '1_10':
        return get1_10()
    elif task_type == "1_8":
        return get1_8()
    elif task_type == "2_11":
        return get3_7()
    elif task_type == "1_19":
        return get4_7()
    elif task_type == '2_8':
        return get2_8()
    elif task_type == '1_11':
        return get2_8()
    else:
        return "Error: task not found."
