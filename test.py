# _*_ coding:utf-8 _*_
class TestP(object):

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

ins = TestP()
print(ins.fee)
ins.fee = 100#  调用set_fee函数
print(ins.get_fee())    # 调用get_fee函数
print(ins.dee)
del ins.fee # 调用delete函数
print(ins.fee)