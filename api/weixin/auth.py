# _*_ coding:utf-8 _*_
from baseresource.greenresource import BaseResource

class AuthWeiXin(BaseResource):

    def __init__(self):
        BaseResource.__init__(self)

    def real_GET(self, request):
        return "微信验证"
        pass