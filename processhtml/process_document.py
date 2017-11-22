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
            SearchIndex.add_index(url.strip(), {'title': title if title else None,
                                                'metadata': description if description else None})
    @classmethod
    def create_index(cls):
        total = 0
        gap = 3
        sql = 'select url, html from document limit  %s,%s' % (total, total+gap)

        results = MysqlDB.run_query(sql)
        if results:
            while results and total < 10:
                for result in results:
                    ProcessDocument.parse_document(result['html'], result['url'])
                total = total + gap
                sql = 'select url, html from document limit  %s,%s' % (total, total + gap)
                results = MysqlDB.run_query(sql)
ProcessDocument.create_index()
for key, value in  SearchIndex.search_index.items():
    print(key)
    for metadata, v in value.items():
        print('\t %s: %s' % (metadata, v))