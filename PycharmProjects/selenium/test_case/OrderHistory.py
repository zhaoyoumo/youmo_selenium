#-*-coding:utf-8-*- 

import time
from selenium import webdriver
import unittest

__author__ = 'Youmo'


class SignIn(unittest.TestCase):
	u"""登录"""

	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.maximize_window()
		self.driver.get("https://test.xjonathan.me/sign-in")
		self.driver.implicitly_wait(30)
		time.sleep(1)
