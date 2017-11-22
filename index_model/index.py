# _*_ coding:utf8 _*_

from lxml import etree


class SearchIndex():

    search_index = {}

    @classmethod
    def add_index(cls, index, data):
        if index not in cls.search_index:
            cls.search_index[index] = data

    @classmethod
    def updata_index(cls, index, data):
        cls.search_index[index] = data


html = etree.fromstring("<title>你好,你怎么了</title>")

title = html.xpath('//title//text()')[0]
from split_query.trie import Trie
print(Trie.parse_query(title))