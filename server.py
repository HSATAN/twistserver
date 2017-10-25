# _*_ coding:utf-8 _*_
from __future__ import print_function
from twisted.internet import reactor
from twisted.web.resource import Resource
from twisted.web.server import Site
from database.conn import PsyBase
import json
from util.common import arg_named

class Root(Resource):

    def __init__(self):
        Resource.__init__(self)
        self.putChild("ajax", App())




class App(Resource):

    def __init__(self):
        Resource.__init__(self)
        self.putChild("third", third())
        self.putChild("userinfo", UserInfo())
        self.putChild("auth", Auth())
        self.putChild("register", Register())
    def render_GET(self, request):
        return "huangkaijie"

class Auth(Resource):
    isLeaf = True
    def render_GET(self, request):
        return json.dumps({"number": 999,"name": "黄开杰", "age": 25, "id": 1, "password": "123456","code": 11111})
    def render_POST(self, request):
        phone_number = arg_named(request, 'phone_number', 0)
        if  phone_number == 0:
            return json.dumps({"code": 20002, "msg": "参数错误"})
        print(phone_number)
        try:

            user = PsyBase.find_user(phone_number)
            if not user:
                return  json.dumps({"code": 20003, "msg": "用户未找到"})
            return json.dumps({"phone_number": 999, "name": "黄开杰", "age": 25, "id": 1, "password": "123456","code": 10000})
        except Exception as e:
            print(e)
            return  json.dumps({"code":2004,"msg": "服务器错误"})

class Register(Resource):

    isLeaf = True
    def render_POST(self, request):
        phone_number = arg_named(request, 'phone_number', 0)
        password = arg_named(request, "password", None)
        name = arg_named(request, "name", None)

        if  phone_number == 0 or password is None or name is None:
            return json.dumps({"code": 20002, "msg": "参数错误"})
        try:

            user = PsyBase.insert_user(phone_number=phone_number,name=name,password=password)
            #return json.dumps({"phone_number": phone_number,"name": name, "age": 25, "id": 1, "password": password,"code": 10000})
            return '10000'
        except Exception as e:
            print(e)
            return  json.dumps({"code":2006,"msg": "注册失败"})


class UserInfo(Resource):
    isLeaf = True
    def render_GET(self, request):

        return json.dumps({"name": "黄开杰", "age": 25, "id": 1, "password": "123456"})

class third(Resource):

    def render_GET(self,request):
        return "third"

if __name__ == '__main__':
    reactor.listenTCP(8888, Site(Root()))
    reactor.run()