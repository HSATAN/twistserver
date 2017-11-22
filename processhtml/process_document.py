# _*_ coding:utf8 _*_

from lxml import etree
from database.mysqldb import MysqlDB
from index_model.index import SearchIndex


class ProcessDocument(object):

    @classmethod
    def parse_document(cls, document,url):
        if document:
            html = etree.HTML(document)
            title = html.xpath("//title/text()")
            if title:
                title = ','.join(title)
            description = html.xpath('//meta[@name="description"]/@content')
            if description:
                description = ','.join(description)
            print(description)
            SearchIndex.add_index(url.strip(), {'title': title, 'metadata': description})
    @classmethod
    def create_index(cls):
        total = 0
        gap = 3
        sql = 'select url, html from document limit  %s,%s' % (total, total+gap)

        results = MysqlDB.run_query(sql)
        if results:
            while results:
                for result in results:
                    ProcessDocument.parse_document(result['html'], result['url'])
                total = total + gap
                sql = 'select url, html from document limit  %s,%s' % (total, total + gap)
                results = MysqlDB.run_query(sql)
ProcessDocument.create_index()
print(SearchIndex.search_index)