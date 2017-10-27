# _*_ coding:utf-8 _*_
from __future__ import print_function
from twisted.web.resource import Resource

def pre_handle_decotor(func):
    def handler(*args, **kwargs):
        print(args)
        print(dir(args[1]))
        print(args[1].getClientIP())
        print(**kwargs)
        print(dir(args[1].args))
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




