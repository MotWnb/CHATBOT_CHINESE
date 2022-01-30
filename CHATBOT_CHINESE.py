# -*- coding: utf-8 -*-
import aiml
import sys
import os
import urllib.request
import urllib
import json

def fy(input1):
    urllib2 = urllib.request
 
    headers = {
    # "Host":"fanyi.youdao.com",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0",
    "Accept":"application/json, text/javascript, */*; q=0.01",
    # "Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    # 以下这个不屏蔽会导致中文不能翻译成英文
    # "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8", 
    "X-Requested-With":"XMLHttpRequest",
    # "Content-Length":"209",
    # "Connection":"keep-alive"
    }
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&sessionFrom="
    key = input1
    formdata = {
	    "i":key,
	    "from":"AUTO",
	    "to":"AUTO",
	    "smartresult":"dict",
	    "client":"fanyideskweb",
	    "salt":"1525335936774",
	    "sign":"5747b87ca68723a7230af9cb648a04c1",
	    "doctype":"json",
	    "version":"2.1",
	    "keyfrom":"fanyi.web",
	    "action":"FY_BY_REALTIME",
	    "typoResult":"false"
    }
    # 转码
    data = urllib.parse.urlencode(formdata).encode(encoding='UTF-8')
    # print(data)
    # 发送请求
    request = urllib2.Request(url,data = data ,headers = headers)
    response = urllib2.urlopen(request)
 
    html = response.read().decode('utf-8')
    # json文件读取
    try:
        target = json.loads(html)
        pass
    except:
        target = {'type': 'EN2ZH_CN',
                  'errorCode': 0,
                  'elapsedTime': 75,
                  'translateResult': [[{'src': "ERROR' , ' e r r o r C o d e ' : 0 , ' e l a p s e d T i m e ' : 0 , ' t r a n s l a.", 'tgt': "ERROR"}]]}
        pass
# 最终字典列表输出
    # print(target["translateResult"][0][0]["tgt"])
 
    
    if target["type"] == 'ZH_CN2EN':
    	return target["translateResult"][0][0]["tgt"]
    elif target["type"] == 'EN2ZH_CN'or 'JA2ZH_CN':
    	return target["translateResult"][0][0]["tgt"]
    # 翻译结束
pass




def get_module_dir(name):
    print("module", sys.modules[name])
    path = getattr(sys.modules[name], '__file__', None)
    print(path)
    if not path:
        raise AttributeError('module %s has not attribute __file__' % name)
    return os.path.dirname(os.path.abspath(path))
 

alice_path = get_module_dir('aiml') + '\\botdata\\alice'

os.chdir(alice_path)  # 切换到语料库所在工作目录

alice = aiml.Kernel()  # 创建机器人alice对象
alice.learn("startup.xml") # 加载...\\botdata\\alice\\startup.xml
alice.respond('LOAD ALICE') # 加载...\\botdata\\alice目录下的语料库
 
while True:
    message = input("输入你的消息 >> ")
    if("exit" == message):
        exit()
    message = fy(message)
    response = alice.respond(message) # 机器人应答
    res = fy(response)
    print(res)
