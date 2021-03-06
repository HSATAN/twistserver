# _*_ coding:utf-8 _*_
class P(object):

    def __init__(self):
        self._fee = None
        self.dee = 1000000
    def get_fee(self):
        return self._fee

    def set_fee(self, value):

        self._fee = value
    def delete(self):
        del self.dee
    fee = property(get_fee, set_fee,delete)  # 当设置和获取，删除fee的时候，调用的是里面的三个函数

ins = P()
print(ins.fee)
ins.fee = 100#  调用set_fee函数
print(ins.get_fee())    # 调用get_fee函数
print(ins.dee)
del ins.fee # 调用delete函数
print(ins.fee)


class Two(object):

    def __init__(self):
        self._temp = 100

    @property
    def temp(self):

        print(" get value ")
        return self._temp
    @temp.setter
    def temp(self, value):
        print("set value")
        self._temp = value

intT = Two()
print(intT.temp)
intT.temp = 200
print(intT._temp)

import random
import time
def fib(n):
    index = 0
    a = 0
    b = 1
    while index < n:
        data = yield b
        print(data)
        a, b = b, a + b
        index += 1
sfib = fib(20)

flag = 0
while flag < 20:
    if(flag == 0):
        sfib.send(None)
    else:
        print(sfib.send(random.uniform(0, 0.9)))
    flag += 1
print(flag)
import gevent

def task(url):
    print(url)

gevent.joinall([gevent.spawn(task, "http://www.myenger.com")])
