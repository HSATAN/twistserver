#  _*_ coding:utf-8 _*_
from baseresource.greenresource import BaseResource
from util.common import arg_named
from twisted.web.static import File
from database.mysqldb import MysqlDB
import json


class Serch(BaseResource):

    def real_GET(self, request):

        word = arg_named(request, 'word')
        if not word:
            with open("static/html/serch.html") as f:
                return f.read()
        else:
            result = MysqlDB.run_query('select * from document where html like  "%%%s%%" limit 10' % word)
            data = []

            for url in result:
                item = {}
                item['url'] = url['url'].strip('"').strip('/')
                data.append(item)
            return json.dumps(data)

class Logo(BaseResource):

    isLeaf = True
    def real_GET(self, request):
        with open('static/logo.jpg', 'rb') as f:
            return f.read()
class StaticFile(BaseResource):

    isLeaf = True

    def real_GET(self, request):
        with open("static/js/search.js") as f:
            return f.read()