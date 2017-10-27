# _*_ coding:utf-8 _*_
from __future__ import print_function
from twisted.web.resource import Resource

def pre_handle_decotor(func):
    def handler(*args, **kwargs):
        print(*args)
        print(**kwargs)
        return func(*kwargs, **kwargs)
    return handler



class BaseResource(Resource):

    @pre_handle_decotor
    def render_HEAD(self, request):
        self.render_GET(request)
        pass

    @pre_handle_decotor
    def render_GET(self, request):
        self.render_GET(request)
        pass

    @pre_handle_decotor
    def render_POST(self, request):
        self.render_POST(request)
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




