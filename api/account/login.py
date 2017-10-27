# _*_ coding:utf-8 _*_
from baseresource.greenresource import BaseResource
class Login(BaseResource):

    isLeaf = True
    def __init__(self):
        BaseResource.__init__(self)

    def real_GET(self, request):
        return "你被装饰器先处理过了"
    pass