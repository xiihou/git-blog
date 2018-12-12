# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import requests
"""
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'zh-CN,zh;q=0.9',
'Cache-Control':'max-age=0',
'Host':'v3-dy.ixigua.com',
'If-Range':'"BF74021BE157EC319DBB6CFCE538DE4B"',
'Proxy-Connection':'keep-alive',
'Range':'bytes=256240-256240',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
"""
class DouyinPipeline(object):
    def process_item(self, item, spider):
        repo=requests.get(item['url'],headers={
            # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            # 'Accept-Encoding': 'gzip, deflate',
            # 'Accept-Language': 'zh-CN,zh;q=0.9',
            # 'Cache-Control': 'max-age=0',
            # 'Host': 'v3-dy.ixigua.com',
            # 'If-Range': '"BF74021BE157EC319DBB6CFCE538DE4B"',
            # 'Proxy-Connection': 'keep-alive',
            # 'Range': 'bytes=256240-256240',
            # 'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',

        }).content
        with open(f"{spider.VIDEO_FLIE_PATH}/{item['name']}.mp4",'wb') as f:
            f.write(repo)
        return item
