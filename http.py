#coding:utf-8
import requests



class Http:

    cookieFile = 'conf/zhihu.cookies'
    agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    headers = {
        "Host": "www.zhihu.com",
        "Referer": "https://www.zhihu.com/",
        'User-Agent': agent
    }

    cookies = ''
    session = ''


    def __init__(self):
        self.cookie(Http.cookieFile)
        self.session = requests.session()


    def cookie(self,file):
        f = open(file, 'r')  # 打开所保存的cookies内容文件
        cs = {}  # 初始化cookies字典变量
        for line in f.read().split(';'):  # 按照字符：进行划分读取
            # 其设置为1就会把字符串拆分成2份
            name, value = line.strip().split('=', 1)
            cs[name] = value  # 为字典cookies添加内容
        self.cookies = cs

    def getHtml(self,url):
        logger.debug("http get:" + url)
        return self.session.get(url,headers=self.headers,cookies=self.cookies)



