
#coding=utf-8

import mitmproxy.http
from mitmproxy import ctx, http
from createDB import get_db

class Faker:
               
    def response(self,flow: mitmproxy.http.HTTPFlow):
        # text = flow.response.get_text()
        # text = text.replace("搜索", "请使用谷歌")
        # flow.response.set_text(text)
        if flow.request.url=='https://www.runoob.com/python/att-string-replace.html':
            print('??????发生了什么')
            
            #flow.response.set_text("<html><head><title>FAIL</title></head><p>他妈的没办法改变部分内容，太难了</p><script>alert('你妈的，为什么')</script></html>")
        aa=flow.response.get_text()
        aa=aa.replace('Python','C++',999)
        bb="<html><head><title>FAIL</title></head><p>helloworld~TEXT</p><a href='http://www.so.com'>touch me</a></html>"
        flow.response.set_text(bb)
        # if flow.request.host == 'www.scut.edu.cn' or flow.request.host == 'jw2005.scuteo.com':
        #     cook=flow.response._get_cookies()
        #     print('这是cookie，不知道有几个诶',cook)
            # flow.response.set_content(bytes("<html><head><title>fail</title></head><p>helloworld~Content</p></html>",'utf-8'))
            #flow.response.set_text("<html><head><title>FAIL</title></head><p>helloworld~TEXT</p><a href='http://www.baidu.com'>touch me</a></html>")

        if flow.request.url.startswith('http://110.65.10.181'):
            bbb=flow.request.url
            print("看我抓到了什么！！！",bbb)
            flow.response.set_text(bytes("<html><head><title>FAIL</title></head><p>helloworld~TEXT</p></html>",'utf-8'))

    
