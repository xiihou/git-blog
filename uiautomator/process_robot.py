#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
一个负责搜集需要发送的信息，
一个负责发送信息，提升效率
多进程 开抖音机器人
"""



import os
import time
import redis
import logging
import uiautomator2 as u2
from multiprocessing import Pool


logging.basicConfig(level=logging.INFO, format='%(asctime)s : %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

loggin = logging.getLogger()

def enter(d,douyin_hao):
	try:
		time.sleep(2)
		loggin.info('解锁...')
		d.unlock()
		time.sleep(2)
		d.app_stop('com.ss.android.ugc.aweme')
		time.sleep(2)
		loggin.info('打开抖音...')
		d.app_start('com.ss.android.ugc.aweme')
		time.sleep(15)
		while True:
			ui_str = d.dump_hierarchy(compressed=True)
			if '用户隐私政策概要' in ui_str:
				loggin.info('用户隐私政策概要')
				d(text='同意').click()
				time.sleep(2)
				continue
			if '长按屏幕使用更多功能' in ui_str:
				loggin.info('长按屏幕使用更多功能')
				d(text='长按屏幕使用更多功能').click(0.2)
				time.sleep(2)
				continue
			if '我知道了' in ui_str:
				loggin.info('我知道了')
				d(text='我知道了').click()
				time.sleep(2)
				continue
			if '以后再说' in ui_str:
				loggin.info('以后再说')
				d(text='以后再说').click()
				time.sleep(2)
				continue
			break
		if '随拍' not in d.dump_hierarchy(compressed=True):
			d.click(0.065, 0.065)
			time.sleep(2)
		else:
			d.click(0.91, 0.073)
			time.sleep(2)
		d(className="android.widget.EditText").send_keys(douyin_hao)
		time.sleep(1)
		d(text="搜索").click()
		time.sleep(2)
		d.xpath(
			'//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.support.v7.widget.RecyclerView/android.widget.LinearLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ImageView').click()
		time.sleep(5)
		ui_str = d.dump_hierarchy()
		if '说点什么' in ui_str:
			loggin.info('到达主播页面...')
			return True
		else:
			return False
	except:
		return False

def collection(serial,douyin_hao):
	os.system(f'python -m uiautomator2 init --serial {serial}')
	d=u2.connect_usb(serial)
	while True:
		if enter(d,douyin_hao):
			break
		continue
	redis_client=redis.Redis(host='148.70.86.158',password='zhouguzhougu')
	fen_set=set()
	guan_set=set()


	while True:
		try:
			ui_str = d.dump_hierarchy()
			if '本场榜' in ui_str:
				d.press("back")
				time.sleep(1)
			if '搜索' in ui_str:
				# d.xpath(
				# 		'//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.widget.LinearLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ImageView').click()
				d.xpath(
					'//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.support.v7.widget.RecyclerView/android.widget.LinearLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ImageView').click()
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
			#欢迎
			dd = d.xpath(
				'//android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView').all()
			if dd:
				text_1 = dd[0].text
				if text_1:
					redis_client.lpush(f'robot:text:{douyin_hao}',f"欢迎{text_1}")
			ddd = d.xpath(
							'//android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout/android.widget.TextView').all()
			if ddd:
				for dddd in ddd:
					text = dddd.text

					if '送出' in text:
						if '嘉年华' in text or '抖音1号' in text or '直升机' in ui_str or '独角兽' in ui_str or '爱心光波枪' in ui_str:
							for _ in range(3):
								redis_client.lpush(f'robot:text:{douyin_hao}',f"感谢{text.strip('0 ').split(': 送出')[0]}送的礼物")
						elif 'Disco' in ui_str:
							for _ in range(2):
								redis_client.lpush(f'robot:text:{douyin_hao}',f"感谢{text.strip('0 ').split(': 送出')[0]}送的礼物")
						else:
							redis_client.lpush(f'robot:text:{douyin_hao}',f"感谢{text.strip('0 ').split(': 送出')[0]}送的礼物")

					if '关注了主播' in text:
						# TODO
						guan_name = text.strip('0 ').split('关注了主播')[0]
						if guan_name not in guan_set:
							guan_set.add(guan_name)
							redis_client.lpush(f'robot:text:{douyin_hao}',f"感谢{guan_name}的关注")
							continue
					if '分享本次直播' in text:
						fen_name=text.strip('0 ').split('分享本次直播')[0]
						if fen_name not in fen_set:
							fen_set.add(fen_name)
							redis_client.lpush(f'robot:text:{douyin_hao}',f"感谢{fen_name}的分享")
							continue

		except Exception as e:
			logging.info(f'ERROR:{e}')
			pass

def sender_text(serial,douyin_hao):
	os.system(f'python -m uiautomator2 init --serial {serial}')
	d=u2.connect_usb(serial)
	while True:
		if enter(d,douyin_hao):
			break
		continue
	redis_client = redis.Redis(host='148.70.86.158', password='zhouguzhougu',decode_responses=True)
	d.set_fastinput_ime(True)
	d(text='说点什么...').click()
	while True:
		text=redis_client.lpop(f'robot:text:{douyin_hao}')
		d.clear_text()
		d.send_keys(text)
		time.sleep(1)
		d.press("enter")
		time.sleep(1)


if __name__ == "__main__":
	douyin_hao='W199161521'
	ps = Pool(2)
	ps.apply_async(collection,args=('127.0.0.1:21533',douyin_hao))
	ps.apply_async(sender_text,args=('127.0.0.1:21523',douyin_hao))
	ps.close()
	ps.join()

