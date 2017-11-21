# _*_ coding:utf8 _*_

dictuser = {}
with open('/Users/huangkaijie/halog/ha1/20171030/haproxy.log-20171030-235900') as f:
    for line in f:
        if '/v2.0/account/signup_number' in line:

            data = line.split(' ')
            dictuser.setdefault(data[5].split(':')[0], 0)
            dictuser[data[5].split(':')[0]] += 1
            print(line)

dictuser = sorted(dictuser.items(), key = lambda value:value[1], reverse=True)
print(dictuser)