 #-*-coding:utf-8-*- 

import time
from selenium import webdriver
import unittest

__author__ = 'Youmo'


class OrderHistory(unittest.TestCase):
	u"""历史委托"""

	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.maximize_window()
		self.driver.get("https://test.xjonathan.me/sign-in")
		self.driver.implicitly_wait(30)
		time.sleep(1)
