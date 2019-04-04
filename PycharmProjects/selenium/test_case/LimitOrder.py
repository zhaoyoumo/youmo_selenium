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
        self.driver.find_element_by_id("account").send_keys("zhaoyoumo@outlook.com")
        self.driver.find_element_by_id("password").send_keys("Abcd1234**")
        self.driver.find_element_by_xpath("//div/div/button").click()
        time.sleep(1)
        self.driver.get("https://test.xjonathan.me/trade")  # 进入交易页面
        self.driver.implicitly_wait(30)
        time.sleep(1)

    def LimitOrder(self, price, size):
        u"""价格和数量参数化"""
        self.driver.find_element_by_xpath("//div[2]/input").send_keys(price)
        self.driver.find_element_by_xpath("//div[3]/input").send_keys(size)
        self.driver.find_element_by_xpath("//button/span[2]").click()
        time.sleep(1)

    def test01(self):
        u"""下限价委托多单，查看当前委托列表"""
        self.driver.find_element_by_css_selector(".form-control:nth-child(1)").send_keys(10)  # 杠杆输入10x
        self.driver.find_element_by_xpath("//div[3]/div[2]/div").click()
        self.LimitOrder(4000, 1000)
        message = self.driver.find_element_by_xpath("//span/div/div/div/div/div").text
        self.assertTrue(message)
        print (u"弹出提示信息：%s" % message)  # 断言实际结果与期望结果一致
        time.sleep(1)
        self.driver.find_element_by_xpath("//div[3]/div/div/ul/li[2]/a/span").click()  # 点击当前委托
        output_price = self.driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div[3]/div/div/div/div[2]/table/tbody/tr/td[2]").text
        input_price = "4000"
        self.assertEqual(output_price, input_price)  # 断言实际结果与期望结果一致
        print (u"委托价格：%s" % output_price)
        output_size = self.driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div[3]/div/div/div/div[2]/table/tbody/tr/td[3]").text
        input_size = "1000"
        self.assertEqual(output_size, input_size)  # 断言实际结果与期望结果一致
        print (u"委托数量：%s" % output_size)

        self.driver.get("https://test.xjonathan.me/wallet/balance")  # 进入我的资产页面
        time.sleep(1)
        result = self.driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div[2]/div/div[3]/div/div/table/tbody/tr[5]/td[2]").text
        order_margin = "0.02537500 BTC"
        self.assertEqual(result, order_margin)  # 断言实际结果与期望结果一致
        print (u"委托保证金：%s" % result)
        time.sleep(2)
        # self.driver.get("https://test.xjonathan.me/trade")
        # self.driver.implicitly_wait(30)
        # self.driver.find_element_by_xpath(u"//span[contains(.,'取消')").click()  # 撤销委托单

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
