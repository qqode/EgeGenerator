import sqlite3
from typing import Union
from random import *
from sqlite3 import *
from fastapi import FastAPI
from math import *
con = sqlite3.connect(
    'tasks.db')
cur = con.cursor()
app = FastAPI()


def get1_7(type):
    size1 = 2 ** randint(7, 13)
    size2 = 2 ** randint(2, 300)
    ex = str(cur.execute('''SELECT q FROM fuck WHERE id=701''').fetchone()[
             0]).format(size1=size1, size2=size2, cl=cl)
    exec((cur.execute('''SELECT a FROM fuck WHERE id=701''').fetchone()[0]).format(
        size1=size1, size2=size2, cl=cl), locals(), globals())
    return otv, ex


def get2_7(type):
    size1 = 2 ** randint(7, 13)
    size2 = 2 ** randint(7, 13)
    v = randint(30, 200)
    ex = str(cur.execute('''SELECT q FROM fuck WHERE id=702''').fetchone()[
             0]).format(size1=size1, size2=size2, v=v)
    exec((cur.execute('''SELECT a FROM fuck WHERE id=702''').fetchone()[0]).format(
        size1=size1, size2=size2, cl=cl), locals(), globals())
    return otv, ex


def get3_7(type):
    dpi2 = randint(100, 300)
    dpi1 = randint(310, 600)
    color1 = randint(16, 24)
    color2 = randint(2, 12)
    sred = randint(10, 100)
    ex = str(cur.execute('''SELECT q FROM fuck WHERE id=703''').fetchone()[
             0].format(dpi1=dpi1, dpi2=dpi2, color1=color1, color2=color2, sred=sred))
    exec((cur.execute('''SELECT a FROM fuck WHERE id=703''').fetchone()[0]).format(
        dpi1=dpi1, dpi2=dpi2, color1=color1, color2=color2, sred=sred), locals(), globals())


def get4_7(type):
    list1 = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
    color = choice(list1)
    size1 = randint(100, 500)
    size2 = randint(100, 500)
    ex = str(cur.execute('''SELECT q FROM fuck WHERE id=704''').fetchone()[
             0].format(color=color, size2=size2, size1=size1))
    exec((cur.execute('''SELECT q FROM fuck WHERE id=704''').fetchone()[
         0].format(color=color, size1=size1, size2=size2)), locals(), globals())


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
