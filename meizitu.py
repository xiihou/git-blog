import requests
import redis
import re
from hashlib import md5
from urllib.parse import urljoin
import os
import time
import random

class Meizi_Flie:
    # path 为图片的保存路径 redis_host 为redis的主机ip
    def __init__(self,url,path=r'E:\img',redis_host='192.168.1.105',port=6379,password=None):
        self.redis_client=redis.Redis(host=redis_host,port=port,password=password)
        self.start_url=url
        self.request=requests.request
        self.headers={
            'user-agent': random.choice(['Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3514.0 Safari/537.36',
                                         'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'])
        }
        self.path=path
        if not os.path.exists(self.path):
            os.makedirs(self.path)

    # 下载
    def download_html(self,url,method='GET'):
        try:
            response=self.request(url=url,method=method,headers=self.headers,timeout=10,)
            return response
        except Exception as e:
            print(e)
            return ""
    #解析 将url 存到redis的list里
    #利用redis的set去重
    def parse_html(self,response,source_url):
        page_url_list = re.findall(r'(?<=href=").*?(?=")',response.text)
        img_url_list=re.findall(r'(?<=src=").*?jpg(?=")',response.text)

        for url in page_url_list:
            if not url.startswith('http'):
                url=urljoin(source_url,url)
            if self.fliter_request(url):
                self.redis_client.lpush('my_flie:request_url_list',url)

        for url in img_url_list:
            if not url.startswith('http'):
                url=urljoin(source_url,url)
            if self.fliter_request(url):
                self.redis_client.lpush('my_flie:request_url_list',url)


    def save_img(self,response,url):
        with open(f'{self.path}\{self.md5_url(url)}.jpg','wb') as f:
            f.write(response.content)

    def fliter_request(self,url):
        flag=self.redis_client.sadd('my_flie:set',url)
        return flag

    def run(self):
        response=self.download_html(self.start_url)
        if response:
            self.parse_html(response,self.start_url)
        else:
            print('出错')
            return
        count=1
        while True:
            time.sleep(1)
            try:
                url=self.redis_client.rpop('my_flie:request_url_list').decode()
                response=self.download_html(url)
                if response:
                    if url.endswith('jpg'):
                        self.save_img(response, url)
                        print(f"下载{count}张")
                        count += 1
                    else:
                        self.parse_html(response, url)
                        print(f"下载页面")

            except Exception as e:
                print(e)


    def md5_url(self,url):
        m=md5()
        m.update(url.encode())
        return m.hexdigest()

    def close(self):
        self.redis_client.delete('my_flie:request_url_list')
        self.redis_client.delete('my_flie:set')


if __name__ == "__main__":
    url='http://www.meizitu.com'   # 这里可以换成你想要爬取的网址
    me=Meizi_Flie(url)
    me.run()





