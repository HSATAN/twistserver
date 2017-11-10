# _*_ coding:utf-8 _*_
from collections import defaultdict
import time
import sys
import json
reload(sys)
sys.setdefaultencoding('utf8')


class Trie(object):

    trie_dict = defaultdict(dict)

    @classmethod
    def create_trie(cls,final_dict, temp_dict):

        if temp_dict.keys()[0] not in final_dict:
            final_dict[temp_dict.keys()[0]]  = temp_dict[temp_dict.keys()[0]]
            return final_dict
        else:
            if final_dict[temp_dict.keys()[0]] == 1:
                final_dict[temp_dict.keys()[0]] = temp_dict[temp_dict.keys()[0]]
                return final_dict
            if temp_dict[temp_dict.keys()[0]] == 1:
                return final_dict
            final_dict = cls.create_trie(final_dict[temp_dict.keys()[0]], temp_dict[temp_dict.keys()[0]])
        return final_dict
    @classmethod
    def create_dict(cls, line=""):
        temp = {}

        for i in range(len(line)-1,-1,-1):
            mid = {}
            if not temp:
                temp[line[i]] = 1
                mid = temp
                continue
            mid[line[i]] = temp
            temp = mid
        return mid

if __name__ == '__main__':
    le = 0
    try:
        f = open('model.txt')
        Trie.trie_dict = json.load(f)
    except:
        print("加载模型失败,重新生成模型")
        i = 0
        with open('H:\\sougoudata\\new_sougou.txt') as f:
            for line in f:

                line = line.strip('\n').decode(encoding='utf8')
                if le<len(line):
                    le = len(line)
                print(i)
                Trie.create_trie(Trie.trie_dict, Trie.create_dict(line))
                i += 1
                # if i > 2:
                #     break
            with open('model.txt', 'w') as f:
                f.write(json.dumps(Trie.trie_dict))
    print(le)

line = raw_input("请输入要解析的语句> ")
while line != 'quit':
    line = line.strip('\n').decode(encoding='utf8')
    line_lenth = len(line)
    print(line_lenth)
    line = raw_input("请输入要解析的语句> ")
    pass