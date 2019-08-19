#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import re
import time
import redis
import random
import logging
import datetime
import pytesseract
import uiautomator2 as u2
from PIL import Image,ImageEnhance


logging.basicConfig(level=logging.INFO, format='%(asctime)s : %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
loggin = logging.getLogger()


REDIS_HOST='127.0.0.1'
REDIS_PORT=6379
REDIS_DB=0
REDIS_USER=""
REDIS_PASSWD=""


class Run():

	def __init__(self,device):
		self.device=device
		self.redis_pool = redis.ConnectionPool(host=REDIS_HOST, password=REDIS_PASSWD, port=REDIS_PORT, db=REDIS_DB,
										max_connections=2)
		self.guan_set=set()
		self.text_list = []


	def run(self):
		while True:
			try:
				loggin.info('开始任务1...')
				loggin.info('初始化服务...')
				os.system(f'python -m uiautomator2 init --serial {self.device}')

				d=u2.connect_usb(self.device)
				time.sleep(2)

				while True:
					text_lust=[]
					try:
						ui_str = d.dump_hierarchy()
						if '本场榜' in ui_str:
							d.press("back")
							time.sleep(1)
						if '搜索' in ui_str:
							try:
								d.xpath(
									'//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.widget.LinearLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ImageView').click()
							except:
								loggin.info('进入直播间失败...')
								d.press("home")
								break
						if '直播已结束' in ui_str:
							loggin.info('直播已结束...')
							d.press("home")
							break
						if '立即赠送' in ui_str:
							d.press("back")
							time.sleep(1)
						if '条新消息' in ui_str:
							d.click(115, 1308)
							time.sleep(3)
						if '说点什么...' not in ui_str and '说点什么' in ui_str:
							d.press("back")
							time.sleep(1)
						if '@TA' in ui_str:
							d.press("back")
							time.sleep(1)
						dd = d.xpath(
							'//android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView').all()
						if dd:
							text_1 = dd[0].text
							if text_1:
								self.text_list.append(text_1.rstrip('进入直播间'))
						ddd = d.xpath(
							'//android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout/android.widget.TextView').all()

						if ddd:
							for dddd in ddd:
								text = dddd.text
								if '送出' in text:
									text_lust.append(f"感谢{text.strip('0 ').split(': 送出')[0]}送的礼物")
								if '关注了主播' in text:
									#TODO
									guan_name=text.strip('0 ').split('关注了主播')[0]

									text_lust.append(f"感谢{guan_name}的关注")
									self.guan_set.add(guan_name)
									continue
								if '分享本次直播' in text:
									text_lust.append(f"感谢{text.strip('0 ').split('分享本次直播')[0]}的分享")
									continue
						loggin.info(text_lust)
						if text_lust:
							d.set_fastinput_ime(True)
							d(text='说点什么...').click()
							time.sleep(1)
							for t in text_lust:
								d.clear_text()
								time.sleep(1)
								d.send_keys(t)
								time.sleep(1)
								d.press("enter")
								time.sleep(1)

							time.sleep(1)
							d.press("back")
							time.sleep(1)
							d.press("back")
					except Exception as e:
						print(e)
						continue
			except Exception as e:
				print(e)
				continue


if __name__=='__main__':
	import sys
	print(os.getpid())
	p=sys.argv
	try:
		device=p[1]
	except:
		exit(1)
	loggin.info(device)
	r=Run(device)
	r.run()
