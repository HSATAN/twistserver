# _*_ coding:utf-8 _*_

from twisted.internet import reactor
from twisted.web.resource import Resource
from twisted.web.server import Site

class Root(Resource):

    def __init__(self):
        Resource.__init__(self)
        self.putChild("ajax",App())


class App(Resource):

    #isLeaf = True
    def __init__(self):
        Resource.__init__(self)
        self.putChild("third", third())
    def render_GET(self, request):
        return "huangkaijie"

class third(Resource):

    def render_GET(self,request):
        return "third"

if __name__ == '__main__':
    reactor.listenTCP(9999, Site(Root()))
    reactor.run()