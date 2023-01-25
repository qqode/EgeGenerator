import sqlite3
from typing import Union
from random import *
from sqlite3 import *
from fastapi import FastAPI
from math import *
from fastapi.middleware.cors import CORSMiddleware
from itertools import *

con = sqlite3.connect(
    'tasks.db', check_same_thread=False)
cur = con.cursor()
app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get1_7():
    cl = randint(2, 300)
    size1 = 2 ** randint(7, 13)
    size2 = 2 ** randint(2, 300)
    ex = str(cur.execute('''SELECT q FROM fuck WHERE id=701''').fetchone()[0]).format(size1=size1, size2=size2, cl=cl)
    exec((cur.execute('''SELECT a FROM fuck WHERE id=701''').fetchone()[0]).format(size1=size1, size2=size2, cl=cl), locals(), globals())
    return {"task": ex, "uid": otv}


def get2_7():
    
    size1 = 2 ** randint(7, 13)
    size2 = 2 ** randint(7, 13)
    v = randint(30, 200)
    ex = str(cur.execute('''SELECT q FROM fuck WHERE id=702''').fetchone()[0]).format(size1=size1, size2=size2, v=v)
    exec((cur.execute('''SELECT a FROM fuck WHERE id=702''').fetchone()[0]).format(size1=size1, size2=size2, v=v), locals(), globals())
    return {"task": ex, "uid": otv}


def get3_7():
    dpi2 = randint(100, 300)
    dpi1 = randint(310, 600)
    color1 = randint(16, 24)
    color2 = randint(2, 12)
    sred = randint(10, 100)
    ex = str(cur.execute('''SELECT q FROM fuck WHERE id=703''').fetchone()[0].format(dpi1=dpi1, dpi2=dpi2, color1=color1, color2=color2, sred=sred))
    exec((cur.execute('''SELECT a FROM fuck WHERE id=703''').fetchone()[0]).format(dpi1=dpi1, dpi2=dpi2, color1=color1, color2=color2, sred=sred), locals(), globals())
    return {"task": ex, "uid": otv}

def get4_7():
    list1 = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
    color = choice(list1)
    size1 = randint(100, 500)
    size2 = randint(100, 500)
    ex = str(cur.execute('''SELECT q FROM fuck WHERE id=704''').fetchone()[0].format(color=color, size2=size2, size1=size1))
    exec((cur.execute('''SELECT a FROM fuck WHERE id=704''').fetchone()[0].format(color=color, size1=size1, size2=size2)), locals(), globals())
    return {"task": ex, "uid": otv}
def get5_7():
    speedA = randint(5, 60)
    res = randint(2, 4)
    cle = randint(2, 4)
    speedB = randint(2, 5)
    ex = str(cur.execute('''SELECT q FROM fuck WHERE id = 705''').fetchone()[0].format(speedB=speedB,speedA=speedA,res=res,cle=cle))
    exec((cur.execute('''SELECT q FROM fuck WHERE id=705''').fetchone()[0].format(speedB=speedB,speedA=speedA,res=res,cle=cle)),locals(),globals())
    return {"task":ex,"uid":otv}
def get1_11():
    slov = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'П', 'Р', 'С', 'Т', '1',
                 '2',
                 '3', '4', '5', '6', '7', '8', '9', 'Я', 'Ч']
    length0 = randint(5, 10)
    chars = []
    leni = 0
    for i in range(1, length0):
        a = choice(slov)
        if a not in chars:
            leni += 1
            chars.append(choice(slov))
            chars.append(' ')
    length_sims = randint(10, 30)
    amount = randint(10, 30)
    chats = ''.join(chars)
    ex = str(cur.execute('''SELECT q FROM fuck WHERE id = 1101''').fetchone()[0].format(length_sims=length_sims,amount=amount,chats=chats))
    exec((cur.execute('''SELECT q FROM fuck WHERE id=1101''').fetchone()[0].format(amount=amount,leni=leni,length_sims=length_sims)),locals(),globals())
    return {"task": ex, "uid": otv}
def get2_11():
    length_sims = randint(10, 30)
    bu = randint(12, 74)
    buic = bu + bu + 10
    amount = randint(10, 50)
    ex = str(cur.execute('''SELECT q FROM fuck WHERE id = 1102''').fetchone()[0].format(length_sims=length_sims,bu=bu,amount=amount))
    exec((cur.execute('''SELECT q FROM fuck WHERE id=1102''').fetchone()[0].format(length_sims=length_sims,buic=buic,amount=amount)),locals(),globals())
    return {"task": ex, "uid": otv}
def get1_19():
    otv = []
    adder1 = randint(1, 8)
    adder2 = randint(1, 8)
    mult = randint(2, 4)
    pit = randint(20, 99)
    ex = str(cur.execute('''SELECT q FROM fuck WHERE id = 1102''').fetchone()[0].format(adder2=adder2,adder1=adder1,mult=mult,pit=int(pit)-1))
    exec((cur.execute('''SELECT q FROM fuck WHERE id=1102''').fetchone()[0].format(pit=pit,mult=mult)),locals(),globals())
    return {"task": ex, "uid": otv}

def get1_8():
    s = []
    place = randint(50, 300)
    set = []
    slov = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'П', 'Р', 'С', 'Т',
                 'Ж', 'Я', 'Ч']
    wordsize = randint(4, 6)
    setsize = randint(4, 6)
    for i in range(setsize):
        set.append(slov.pop(slov.index(choice(slov))))
    set1 = '(' + ''.join(set) + ')'
    set = sorted(set)
    perebor = product(set, repeat=int(wordsize))
    for i in perebor:
        s.append(i)
    ex=str(cur.execute('''SELECT q FROM fuck WHERE id = 801''').fetchone()[0].format(set1=set1,wordsize=wordsize,s=s,place=place))
    exec((cur.execute('''SELECT a FROM fuck WHERE id=801''').fetchone()[0].format(s=s,place=place)),locals(),globals())
    return {"task": ex, "uid": otv}
def get2_8():
    setr = []
    s = []
    choose = choice(('гласной', 'согласной'))
    slov = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'П', 'Р', 'С', 'Т', 'O',
                 'Ж', 'Я', 'Ч']
    vovs = ['A', 'E', 'Ё', 'И', 'О', 'Я']
    cons = ['Б', 'В', 'Г', 'Д', 'Ж', 'З', 'Й', 'К', 'Л', 'М', 'Н', 'П', 'Р', 'С', 'Т', 'Ж', 'Ч']
    wordsize = randint(4, 6)
    setsize = randint(4, 6)
    otv = 0
    for i in range(setsize):
        setr.append(slov.pop(slov.index(choice(slov))))
        perebor = product(''.join(set), repeat=int(wordsize))
        k = 0
        gl = 0
        for i in perebor:
            k += 1
            if i[0] in vovs:
                gl += 1
            s.append(i)
    if choose == 'гласной':
        exec('''otv=len(set(setr) & set(vovs)) * setsize ** (wordsize - 1)''') # переписать под sql
    else:
        exec('''otv=len(set(setr) & set(cons)) * setsize ** (wordsize - 1)''')
    ex = str(cur.execute('''SELECT q FROM fuck WHERE id = 802'''))
    return {"task": ex, "uid": otv}


@app.get('/getTask')
def getTask(task_type):
    if task_type == "1_7":
        return get1_7()
    elif task_type == "2_7":
        return get2_7()
    elif task_type == "3_7":
        return get3_7()
    elif task_type == "4_7":
        return get4_7()
    else:
        return "error"