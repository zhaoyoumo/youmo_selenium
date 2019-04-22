# -*-coding:utf-8-*-
import unittest

import time
from selenium import webdriver

__author__ = 'Youmo'


class LimitOrder(unittest.TestCase):
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
        u"""价格和数量参数化"""
        self.driver.find_element_by_xpath("//div[2]/input").send_keys(price)    # 输入价格
        self.driver.find_element_by_xpath("//div[3]/input").send_keys(size)     # 输入数量
        self.driver.find_element_by_xpath("//button/span[2]").click()           # 点击买入
        time.sleep(1)

    def test01(self):
        u"""价格输入为空"""
        self.LimitBuyOrder('', 1000)
        message = self.driver.find_element_by_xpath("//span/div/div/div/div/div").text
        self.assertTrue(message)
        print (u"弹出提示信息：%s" % message)  # 断言实际结果与期望结果一致

    def test02(self):
        u"""数量输入为空"""
        self.LimitBuyOrder(4000, '')
        message = self.driver.find_element_by_xpath("//span/div/div/div/div/div").text
        self.assertTrue(message)
        print (u"弹出提示信息：%s" % message)  # 断言实际结果与期望结果一致

    def test03(self):
        u"""价格、数量为空"""
        self.LimitBuyOrder('', '')
        message = self.driver.find_element_by_xpath("//span/div/div/div/div/div").text
        self.assertTrue(message)
        print (u"弹出提示信息：%s" % message)  # 断言实际结果与期望结果一致

    def test04(self):
        u"""价格输入为0"""
        self.LimitBuyOrder(0, 1000)
        message = self.driver.find_element_by_xpath("//span/div/div/div/div/div").text
        self.assertTrue(message)
        print (u"弹出提示信息：%s" % message)  # 断言实际结果与期望结果一致

    def test05(self):
        u"""数量输入为0"""
        self.LimitBuyOrder(4000, 0)
        message = self.driver.find_element_by_xpath("//span/div/div/div/div/div").text
        self.assertTrue(message)
        print (u"弹出提示信息：%s" % message)  # 断言实际结果与期望结果一致

    def test06(self):
        u"""价格输入字母"""
        self.LimitBuyOrder("aaa", 1000)
        message = self.driver.find_element_by_xpath("//span/div/div/div/div/div").text
        self.assertTrue(message)
        print (u"弹出提示信息：%s" % message)  # 断言实际结果与期望结果一致

    def test07(self):
        u"""价格输入符号"""
        self.LimitBuyOrder("****", 1000)
        message = self.driver.find_element_by_xpath("//span/div/div/div/div/div").text
        self.assertTrue(message)
        print (u"弹出提示信息：%s" % message)  # 断言实际结果与期望结果一致

    def test08(self):
        u"""数量输入字母"""
        self.LimitBuyOrder(4000, "aaaa")
        message = self.driver.find_element_by_xpath("//span/div/div/div/div/div").text
        self.assertTrue(message)
        print (u"弹出提示信息：%s" % message)  # 断言实际结果与期望结果一致

    def test09(self):
        u"""数量输入符号"""
        self.LimitBuyOrder(4000, "*****")
        message = self.driver.find_element_by_xpath("//span/div/div/div/div/div").text
        self.assertTrue(message)
        print (u"弹出提示信息：%s" % message)  # 断言实际结果与期望结果一致

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()


# def test01(self):
#     '''判断 a == b '''
#     a = 1
#     b = 1
#     self.assertEqual(a, b)
#
# def test02(self):
#     '''判断 a in b '''
#     a = "hello"
#     b = "hello world!"
#     self.assertIn(a, b)
# ；
# def test03(self):
#     '''判断 a is True '''
#     a = True
#     self.assertTrue(a)
#
# def test04(self):
#     '''失败案例'''
#     a = "悠悠"
#     b = "yoyo"
#     self.assertEqual(a, b)
