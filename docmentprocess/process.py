# _*_ coding:utf8 _*_

from database.mysqldb import MysqlDB

result = MysqlDB.query_all("select url, html from document limit 10")
if result:
    for item in result:
        print(item['url'])