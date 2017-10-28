# _*_ coding:utf-8 _*_
from baseresource.greenresource import BaseResource
from lxml import etree

class AuthWeiXin(BaseResource):

    def __init__(self):
        BaseResource.__init__(self)

    def real_GET(self, request):
        print(dir(request))
        print(request.content.read())
        return "weixinyanzhegn"
        receiveData = request.body.decode('utf8')
        print(receiveData)
        data = etree.fromstring(receiveData)
        ToUserName = data.find('ToUserName').text
        FromUserName = data.find('FromUserName').text
        CreateTime = data.find('CreateTime').text
        # Content = data.find('Content').text
        Content = '我爱熊麟茹'
        # print(receiveData)
        message = '''<xml>
        <ToUserName><![CDATA[{0}]]></ToUserName>
        <FromUserName><![CDATA[{1}]]></FromUserName>
        <CreateTime>{2}</CreateTime>
        <MsgType><![CDATA[text]]></MsgType>
        <Content><![CDATA[{3}]]></Content>
        </xml>'''.format(FromUserName, ToUserName, CreateTime, Content)
        return message
