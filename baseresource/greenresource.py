# _*_ coding:utf-8 _*_
from __future__ import print_function
from twisted.web.resource import Resource
from dataredis.redisconn import BaseRedis
import json
from config import errorcode

def ban_user():
    #   返回异常信息
    return json.dumps({"code": errorcode.TYPES.BAN,"msg":"对不起，由于你操作异常，我们暂时不能为你提供服务"})



def pre_handle_decotor(func):
    #    记录和检测用户的访问频率，如果用户访问次数超过限制，则不返回有效信息
    def handler(*args, **kwargs):
        ip = '00000000'
        try:
            ip = args[1].getHeader('X-Real-IP').strip('')
            if int(BaseRedis.r.get(ip)) > 1000:
                print("此ip已经被限制访问 %s" % ip)
                return ban_user()
        except Exception as e:

            print(e)
        BaseRedis.update(ip,1)

        return func(*args, **kwargs)
    return handler



class BaseResource(Resource):

    @pre_handle_decotor
    def render_HEAD(self, request):
        return self.real_HEAD(request)
        pass

    @pre_handle_decotor
    def render_GET(self, request):
        return self.real_GET(request)
        pass

    @pre_handle_decotor
    def render_POST(self, request):
        return self.real_POST(request)
        pass

    @pre_handle_decotor
    def real_HEAD(self, request):
        pass

    @pre_handle_decotor
    def real_GET(self, request):
        pass

    @pre_handle_decotor
    def real_POST(self, request):
        pass





