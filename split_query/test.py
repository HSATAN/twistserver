# _*_ coding:utf8 _*_

from trie import Trie
Trie.load_model()
line = raw_input("请输入要解析的语句> ")
Trie.parse_query(line)
line = raw_input("请输入要解析的语句> ")