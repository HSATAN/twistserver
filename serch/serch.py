#  _*_ coding:utf-8 _*_
from baseresource.greenresource import BaseResource
from util.common import arg_named
from twisted.web.static import File
from database.mysqldb import MysqlDB
import json
import logging
from index_model.index import SearchIndex
class Serch(BaseResource):

    def real_GET(self, request):

        word = arg_named(request, 'word')
        if not word:
            logging.info("访问搜索首页")
            with open("static/html/serch.html") as f:
                return f.read()
        else:
            logging.info("搜索关键词为:%s" %word)
            sql_full_index = 'SELECT * from document WHERE MATCH(html) AGAINST ("%s" in NATURAL LANGUAGE MODE)' % word
            sql = 'select * from document where html like  "%%%s%%" limit 10' % word
            result = MysqlDB.run_query(sql)
            data = []
            if not result:
                return json.dumps([])
            for url in result:
                item = {}
                item['url'] = url['url'].strip('"').strip('/')
                try:
                    item['metadata'] = SearchIndex.search_index[url['url']]
                except Exception as e:
                    logging.error("get metadata error %s" % e)
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