
#coding=utf-8

import time
import mitmproxy.http
from createDB import get_db

class Faker:
               
    def response(self,flow: mitmproxy.http.HTTPFlow):
 
        #part A:访问scut相关网站时，一律访问失败
        if flow.request.host=='www.scut.edu.cn':
            flow.response.set_text(
                '''
                <html>
                <head><title>FAIL！</title></head>
                <body>
                    <p style="margin-top: 80px; margin-left: 50px; font-size: 24px;">报告老板！所有华工host下的的网站都访问不了了！除了计院↓</p>
                    <a href='http://cs.scut.edu.cn' style="color:red;font-size: 14px;margin-left: 150px;">不点我我也会自己跳过去，哼</a>
                    <h1 type="text" id='clock' style='color:blue;position: fixed;left: 40%; top: 50%'>3</h1>
                    <h1 style='color:blue;float: left;position: fixed;left: 42.7%; top: 49.5%''>秒后自动跳转</h1>
                </body>
                <script> 
                    var t=5;
                    function clock(){ t=t-1; document.getElementById('clock').innerHTML=t; setTimeout('clock()',1000);} 
                    function jumpToCS(){ window.location.href='http://cs.scut.edu.cn'}
                    clock(); 
                    setTimeout('jumpToCS()',4000); 
                </script>
                </html>
                '''
            )

        #part B:访问学院网站时，修改头部logo为一段话
        if flow.request.host=='cs.scut.edu.cn':
            text=flow.response.get_text()
            text=text.replace('<a href="/newcs/index.html"></a>','<p style="color:white;font-size:24px; ">第一个是整个替换response，这个展示的是寻找res中的内容并部分替换</p>')
            flow.response.set_text(text)

        #part C:记录下教师信息
        #通过后面的endswith，就可以筛选掉PUBL，空白的那些请求
        if flow.request.path.startswith("/szdw") and flow.request.path.endswith('.xhtml'):
               
            #建立到MySQL的游标
            conn=get_db()
            cursor=conn.cursor()
            isJS=flow.request.path.find('/js/')
            isFJS=flow.request.path.find('/jsjfg/')
            isJSZJ=flow.request.path.find('/jszj/')

            #寻找姓名的位置并截取出来，并给初始化以免不存在而报错（虽然应该没这种情况）
            nameLocation=0
            teacherName='找不到结果' 
            nameLocation=flow.response.text.find('class="NewsTitle">')+18
            teacherName=str(flow.response.text[nameLocation:nameLocation+3])

            if teacherName=='PUB':
                #因为在教授那一栏有区分外聘之类的，所以这里要处理一下
                return
            if teacherName.endswith("\n"):
                #困扰许久...这个是对于两字的处理
                #isspace没用，replace""没用，以为这样写换行符也不对，其实是因为少加了冒号...
                teacherName=teacherName[0:2]

            teacherType=("教授" if (isJS==5) else ("副教授" if (isFJS==5) else "讲师助教"))
            url=flow.request.url
            recordTime=str(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))

            try:
                cursor.execute(
                    'INSERT INTO teacherinfo (name,type,url,recordTime)'
                    ' VALUES (%s,%s,%s,%s)',(teacherName,teacherType,url,recordTime)
                )
                conn.commit()
                conn.close()
            except:
                raise

