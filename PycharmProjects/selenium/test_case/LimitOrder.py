#-*-coding:utf-8-*-
import unittest

import time
from selenium import webdriver
__author__ = 'Youmo'


class LimitOrder(unittest.TestCase):
    u'''进入交易页面'''
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://test.xjonathan.me/sign-in")
        self.driver.find_element_by_id("account").send_keys("zhaoyoumo@outlook.com")
        self.driver.find_element_by_id("password").send_keys("Abcd1234**")
        self.driver.find_element_by_xpath("//div/div/button").click()
        time.sleep(1)
        self.driver.get("https://test.xjonathan.me/trade")  # 进入交易页面
        self.driver.implicitly_wait(30)
        time.sleep(1)

    def LimitOrder(self,price,size):
        u'''价格和数量参数化'''
        self.driver.find_element_by_xpath("//div[2]/input").send_keys(price)
        self.driver.find_element_by_xpath("//div[3]/input").send_keys(size)
        self.driver.find_element_by_xpath("//button/span[2]").click()
        time.sleep(3)

    def test01(self):
        u'''输入杠杆'''
        self.driver.find_element_by_css_selector(".form-control:nth-child(1)").send_keys(10)    # 杠杆输入10x
        self.driver.find_element_by_xpath("//div[3]/div[2]/div").click()
        time.sleep(1)
        self.LimitOrder(4000, 1000)
        message = self.driver.find_element_by_xpath("//span/div/div/div/div/div").text
        self.assertTrue(message)     # 断言实际结果与期望结果一致



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
    #
    # def test03(self):
    #     '''判断 a is True '''
    #     a = True
    #     self.assertTrue(a)
    #
    # def test04(self):
    #     '''失败案例'''
    #     a = "上海-悠悠"
    #     b = "yoyo"
    #     self.assertEqual(a, b)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__" :
    unittest.main()

