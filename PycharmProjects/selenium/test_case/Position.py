# -*-coding:utf-8-*-
import time
import unittest

from selenium import webdriver

__author__ = 'Youmo'


class Position(unittest.TestCase):
    u"""进入交易页面"""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://test.xjonathan.me/sign-in")
        self.driver.find_element_by_xpath("//input[@id='account']").send_keys("zhaoyoumo@outlook.com")
        self.driver.find_element_by_xpath("//input[@id='password']").send_keys("Abcd1234**")
        self.driver.find_element_by_xpath("//div/div/button").click()
        time.sleep(1)
        self.driver.get("https://test.xjonathan.me/trade")  # 进入交易页面
        self.driver.implicitly_wait(30)
        time.sleep(1)

    def LimitBuyOrder(self, price, size):
        u"""限价买单"""
        self.driver.find_element_by_xpath("//div[2]/input").send_keys(price)  # 输入价格
        self.driver.find_element_by_xpath("//div[3]/input").send_keys(size)  # 输入数量
        self.driver.find_element_by_xpath("//button/span[2]").click()  # 点击买入
        time.sleep(1)

    def LimitSellOrder(self, price, size):
        u"""限价卖单"""
        self.driver.find_element_by_xpath("//div[2]/input").send_keys(price)  # 输入价格
        self.driver.find_element_by_xpath("//div[3]/input").send_keys(size)  # 输入数量
        self.driver.find_element_by_xpath("//div/div/button").click()  # 点击卖出
        time.sleep(1)