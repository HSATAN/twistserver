#  _*_ coding:utf-8 _*_
from baseresource.greenresource import BaseResource
from util.common import arg_named
from twisted.web.static import File


class Serch(BaseResource):

    def real_GET(self, request):

        word = arg_named(request, 'word')
        if not word:
            with open("static/serch.html") as f:
                return f.read()
        else:
            return "这是搜索结果"
