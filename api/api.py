# _*_ coding:utf-8 _*_

from api.account.login import Login
from baseresource.greenresource import BaseResource
class Api(BaseResource):

    def __init__(self):
        BaseResource.__init__(self)
        self.putChild("login", Login())

    pass