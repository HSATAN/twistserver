# _*_ coding:utf-8 _*_
from baseresource.greenresource import BaseResource
from lxml import etree
import sys
class AuthWeiXin(BaseResource):

    def __init__(self):
        BaseResource.__init__(self)
    def real_POST(self, request):
        receiveData = request.content.read() #获取微信发送过来的body
        print(receiveData)
        data = etree.fromstring(receiveData)
        ToUserName = data.find('ToUserName').text
        FromUserName = data.find('FromUserName').text
        CreateTime = data.find('CreateTime').text
        Content = data.find('Content').text
        print(Content)
        # print(receiveData)
        message = '<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType><![CDATA[text]]></MsgType><Content><![CDATA[%s]]></Content></xml>'%(FromUserName, ToUserName, CreateTime, Content)
        print(message)
        return message.encode(encoding='utf-8')
    def real_GET(self, request):
        try:
            echostr = request.args.get('echostr')[0]
            return echostr
        except Exception as e:
            print("微信验证失败")