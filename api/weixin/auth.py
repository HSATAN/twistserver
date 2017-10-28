# _*_ coding:utf-8 _*_
from baseresource.greenresource import BaseResource
from lxml import etree

class AuthWeiXin(BaseResource):

    def __init__(self):
        BaseResource.__init__(self)
    def real_POST(self, request):
        print(dir(request))
        print()
        receiveData = request.content.read() #获取微信发送过来的body
        print(receiveData)
        data = etree.fromstring(receiveData)
        ToUserName = data.find('ToUserName').text
        FromUserName = data.find('FromUserName').text
        CreateTime = data.find('CreateTime').text
        Content = data.find('Content').text
        # print(receiveData)
        message = '''<xml>
                <ToUserName><![CDATA[{0}]]></ToUserName>
                <FromUserName><![CDATA[{1}]]></FromUserName>
                <CreateTime>{2}</CreateTime>
                <MsgType><![CDATA[text]]></MsgType>
                <Content><![CDATA[{3}]]></Content>
                </xml>'''.format(FromUserName, ToUserName, CreateTime, Content)
        return message
    def real_GET(self, request):
        try:
            echostr = request.args.get('echostr')[0]
            return echostr
        except Exception as e:
            print("微信验证失败")