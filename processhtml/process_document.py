# _*_ coding:utf8 _*_

from lxml import etree
from database.mysqldb import MysqlDB
from index_model.index import SearchIndex
import logging
import json


class ProcessDocument(object):

    @classmethod
    def parse_document(cls, document,url):
        try:
            if document:
                html = etree.HTML(document)
                title = html.xpath("//title/text()")
                if title:
                    title = ','.join(title)
                description = html.xpath('//meta[@name="description"]/@content')
                if description:
                    description = ','.join(description)
                print(description)
                SearchIndex.add_index(url.strip(), {'title': title if title else None,
                                                    'metadata': description if description else None})
        except Exception as e:
            logging.error("parse document error %s " % e)
    @classmethod
    def create_index(cls):
        try:
            with open('index_model.txt') as model:

                SearchIndex.search_index = json.load(model)

        except Exception as e:
            logging.error("load search_index model error %s" % e)
            sql = 'select url, html from document'
            results = MysqlDB.run_query(sql)
            if results:
                for result in results:
                    ProcessDocument.parse_document(result['html'], result['url'])
            with open('index_model.txt', 'w') as f:
                f.write(json.dumps(SearchIndex.search_index))
ProcessDocument.create_index()