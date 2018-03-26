# _*_ coding:utf-8 _*_
import sys
from twisted.internet import reactor
from twisted.web.resource import Resource
from twisted.web.server import Site
try:
    from database.conn import PsyBase
except:
    pass
import json
import config
import logging
import re
from serch.serch import Serch, StaticFile, Logo
from util.common import arg_named
from api.api import Api
from api.weixin.auth import AuthWeiXin

back_data = "你好"
with open('honglou.txt') as f:
    data = f.read()
    data = data.split('　　')
    back_data = list(set(data))
    back_data.remove('')
print("-----------服务器启动")

class Root(Resource):

    def __init__(self):
        Resource.__init__(self)
        self.putChild("ajax", App())
        self.putChild("api", Api())
        self.putChild("", AuthWeiXin(back_data))
        self.putChild("search", Serch())
        self.putChild("static", StaticFile())
        self.putChild("logo", Logo())




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

    def render_POST(self, request):
        phone_number = arg_named(request, 'phone_number', 0)
        if  phone_number == 0:
            return json.dumps({"code": 20002, "msg": "参数错误"})
        print(phone_number)
        try:

            user = PsyBase.find_user(phone_number)
            if not user:
                return  json.dumps({"code": 20003, "msg": "用户未找到"})
            return json.dumps({"phone_number": phone_number, "name": user['name'],
                               'intro': user['intro'],
                               "age": user['age'], "id": user['id'], "password": "123456","code": 10000})
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
        if len(str(phone_number)) != 11:
            return json.dumps({"code": 20008,"msg": "手机号码不符合格式"})
        try:
            #return json.dumps({"phone_number": phone_number,"name": name, "age": 25, "id": 1, "password": password,"code": 10000})
            code = PsyBase.insert_user(phone_number=phone_number,name=name,password=password)
            print(code)
            return str(code)

        except Exception as e:
            print(e)
            return  json.dumps({"code":2006,"msg": "注册失败"})


class UserInfo(Resource):
    isLeaf = True
    def render_GET(self, request):
        phone_number = arg_named(request, 'phone_number', 0)

        try:

            user = PsyBase.find_user(phone_number)
            if not user:
                return  json.dumps({"code": 20003, "msg": "用户未找到"})
            return json.dumps({"phone_number": phone_number, "name": user['name'],
                               'intro': user['intro'],
                               "age": user['age'], "id": user['id'], "password": "123456","code": 10000})
        except Exception as e:
            print(e)
            return  json.dumps({"code": 2004, "msg": "服务器错误"})

class third(Resource):

    isLeaf = True
    def render_GET(self,request):
        self.write({'name': '黄开杰'})
        self.finish()

if __name__ == '__main__':
    logfile = 'log'
    # try:
    #     from processhtml.process_document import ProcessDocument
    #     ProcessDocument.create_index()
    # except:
    #     pass
    try:
        import platform
        if 'linux' in platform.system().lower():

            logfile = '/home/log/twistserverlog/log'
    except:
        pass
    formats = '[%(asctime)s] [%(filename)s L%(lineno)d] [%(levelname)s] %(message)s'
    logging.basicConfig(level=logging.INFO, format=formats, filename=logfile)
    reactor.listenTCP(8888, Site(third()))
    reactor.run()