# _*_ coding:utf-8 _*_
from __future__ import print_function
from twisted.web.resource import Resource
from dataredis.redisconn import BaseRedis
import json
from config import errorcode
def ban_user():


    return json.dumps({"code": errorcode.TYPES.BAN})



def pre_handle_decotor(func):
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





