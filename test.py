# _*_ coding:utf-8 _*_

with open('hlm') as f:
    data = f.read()
    data = data.split('\n')
    back_data = list(set(data))
print(back_data[1])
print(len(back_data))