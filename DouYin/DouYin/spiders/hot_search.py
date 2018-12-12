# -*- coding: utf-8 -*-
import scrapy
import datetime
from urllib.parse import urlencode
import json
import copy

class HotSearchSpider(scrapy.Spider):
    VIDEO_FLIE_PATH=r'E:\英雄时刻'
    name = 'hot_search'
    allowed_domains = ['api.amemv.com']
    start_urls = ['http://api.amemv.com/']
    custom_settings = {
        'LOG_LEVEL': 'INFO',
        # 'LOG_FILE': ,
        'PROXY_NUM': 1,
        'ROBOTSTXT_OBEY': False,}

    def parse(self, response):
        datas=json.loads(response.text)
        if datas['status_code'] == 0:
            self.logger.info(f"获取热搜成功，开始下载视频。。。")
            for data in datas['aweme_list']:
                item={}
                item['name']=data['aweme_info']['desc']
                item['url']=data['aweme_info']['video']['bit_rate'][0]['play_addr']['url_list'][0]
                self.logger.info(f"开始下载：{item['name']} \n {item['url']}")
                yield item

    def parse_video_url(self,response):
        item=copy.deepcopy(response.meta.get('item'))


    def start_requests(self):
        parames={
            'version_code': '3.4.0',
            'pass-region': '1',
            'pass-route': '1',
            'js_sdk_version': '1.3.0.1',
            'app_name': 'aweme',
            'vid': '88C2FBAB-9616-4FF4-B8CF-DD572D7B8450',
            'app_version': '3.4.0',
            'device_id': '40515002550',
            'channel': 'App Store',
            'aid': '1128',
            'screen_width': '750',
            'openudid': 'd6b77433cb590d9b1a71139b17e257ac903eeaa6',
            'os_api': '18',
            'ac': 'WIFI',
            'os_version': '11.2.1',
            'device_platform': 'iphone',
            'build_number': '34008',
            'iid': '54011121369',
            'device_type': 'iPhone7,2',
            'idfa': '205FB8E5-5BB9-4A4A-8C70-15551BBD3B60',
            'mas': '015b54df5a745d7af8d5fc4b233961cf578b4ef15b007673aed6a8',
            'as': 'a1d5455111173c2f604018',
            'ts': str(int(datetime.datetime.now().timestamp())),
        }
        url=f"https://api.amemv.com/aweme/v1/hotsearch/aweme/billboard/?{urlencode(parames)}"
        yield scrapy.Request(url)