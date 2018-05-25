#!/user/bin/env python
#-*- coding:utf-8 -*-

class UrlManager(object):
	def __init__(self):
		self.new_urls = set()
		self.old_urls = set()
		#初始化两个url列表，set可以去重
	
	#加进一个新url
	def add_new_url(self,url):
		if url is None:
			return 
		if url not in self.new_urls and url not in self.old_urls:
			self.new_urls.add(url)
	
	#加进一些url	
	def add_new_urls(self,url):
		if urls is None or len(urls) == 0:
			return 
		for url in urls:
			self.add_new_url(url)
	
	#判断是否有未爬去的url
	def has_new_url(self):
		return len(self.new_urls) != 0
	
	#取出一个未爬去的url
	def get_new_url(self):
		new_url = self.new_urls.pop()
		self.old_urls.add(new_url)
		return new_url
