# _*_ coding:utf-8 _*_
from collections import defaultdict
import time
sougou_line = 0
new_file = open('H:\\sougoudata\\new_sougou.txt', 'w')
word_dict = defaultdict(lambda : 0)
with open('H:\\sougoudata\\sougou.txt') as f:
    for line in f:
        for word in line.split('\t')[0].split('-'):
            flag = word_dict[word]
            if flag == 0:
                new_file.write(word + '\n')
            word_dict[word] = 1

        sougou_line += 1
        if sougou_line % 1000000 == 0:
            print('%s 百万' % str(int(sougou_line)/int(1000000)))
            time.sleep(3)
        print(sougou_line)
new_file.close()