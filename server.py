# _*_ coding:utf-8 _*_

from twisted.internet import reactor
from twisted.web.resource import Resource
from twisted.web.server import Site

class Root(Resource):

    def __init__(self):
        Resource.__init__(self)
        self.putChild("ajax", App())




class App(Resource):

    def __init__(self):
        Resource.__init__(self)
        self.putChild("third", third())
        self.putChild("userinfo",)

    def render_GET(self, request):
        return "huangkaijie"

class UserInfo(Resource):
    isLeaf = True
    def render_GET(self, request):
        return {""}

class third(Resource):

    def render_GET(self,request):
        return "third"

if __name__ == '__main__':
    reactor.listenTCP(8888, Site(Root()))
    reactor.run()