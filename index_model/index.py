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

