# _*_ coding:utf8 _*_
from collections import defaultdict
import time
in_dict_ip = defaultdict(dict)
in_dict_device = defaultdict(lambda : 0)
with open('/Users/huangkaijie/userdetect/signin.txt') as signin:
    for line in signin:
        data = line.strip('" \n }').split(' ')

        in_dict_ip[data[7]].setdefault('time', 0)
        in_dict_ip[data[7]].setdefault(data[-1], 0)
        in_dict_ip[data[7]].setdefault("uid", set())
        first_login_time = data[0].split('[')[-1] + ' ' + data[1].split(',')[0]

        in_dict_ip[data[7]].setdefault("first_login_time", first_login_time)
        in_dict_ip[data[7]].setdefault("last_login_time", first_login_time)
        if time.mktime(time.strptime(in_dict_ip[data[7]]["first_login_time"], '%Y-%m-%d %H:%M:%S')) > time.mktime(time.strptime(first_login_time, '%Y-%m-%d %H:%M:%S')):
            in_dict_ip[data[7]]["first_login_time"] = first_login_time
        if time.mktime(time.strptime(in_dict_ip[data[7]]["last_login_time"], '%Y-%m-%d %H:%M:%S')) < time.mktime(time.strptime(first_login_time, '%Y-%m-%d %H:%M:%S')):
            in_dict_ip[data[7]]["last_login_time"] = first_login_time
        in_dict_ip[data[7]]['time'] += 1
        in_dict_ip[data[7]][data[-1]] += 1
        in_dict_ip[data[7]]['uid'].add(data[9])
        in_dict_device[data[-1]] += 1

in_dict_ip = sorted(in_dict_ip.items(), key=lambda values: values[1]['time'], reverse=True)
in_dict_device = sorted(in_dict_device.items(), key=lambda value:value[1],reverse=True)
print(in_dict_ip[:200])

