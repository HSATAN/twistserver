#  _*_ coding:utf-8 _*_


"""
计算编辑距离，找出拼写错误




用发音规则编码英文单词，进而进行编写纠错：编码的目的是减少比较的词汇，加快速度

编码规则
1:保留第一个字母（用大写字母）
2：用连字符替换    a,e,i,o,u,y,h,w
3：用数字替换下面这些字母：
    1：b,f,p,v
    2: c,g,j,k,q,s,x,z
    3: d,t
    4: l
    5: m,n
    6: r

4：删除相邻的重复数字
5：删除连字符
6：保留前三个数字或用0延长到三个字符。
"""


def soundex(word=None):

    if not word:
        return None
    if len(word) == 1:
        return word.upper()
    soundexcode = word[1:]

    replace_dict = {1: ['b', 'f', 'p', 'v'],
                    2: ['c', 'g', 'j', 'k', 'q', 's', 'x', 'z'],
                    3: ['d', 't'],
                    4: ['l'],
                    5: ['m', 'n'],
                    6: ['r'],
                    '-': ['a', 'e', 'i', 'o', 'u', 'y', 'h', 'w']}
    for key, value in replace_dict.items():  # 替换
        for character in value:
            soundexcode = soundexcode.replace(character, str(key))
    soundexcode = word[0].upper() + soundexcode

    #   删除
    word = ""
    temp = None
    for character in soundexcode:
        if not temp:
            temp = character
            word += character
            continue
        if character == temp and temp.isdigit():
            temp = character
            continue
        temp = character
        word += character
    word = word.replace("-", "")[:4]
    if len(word) == 1:
        word += '000'
    elif len(word) == 2:
        word += '00'
    elif len(word) == 3:
        word += '0'
    return word

word = raw_input(">>>>>")
while word != 'quit':
    print(soundex(word))
    word = raw_input(">>>>>")