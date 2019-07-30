# -*-coding:utf-8-*-
import unittest

import time
from selenium import webdriver

__author__ = 'Youmo'


class LimitOrder(unittest.TestCase):
    u"""下单操作-限价买单"""
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://test.xjonathan.me/login")
        self.driver.implicitly_wait(30)
        time.sleep(1)
        self.driver.find_element_by_id("account").send_keys("zhaoyoumo@outlook.com")
        self.driver.find_element_by_id("password").send_keys("Abcd1234**")
        self.driver.find_element_by_xpath("//div/div/button").click()  # 登录
#        self.driver.find_element_by_xpath("//form/div/div/button").click()  # 选择验证方式
        self.driver.find_element_by_xpath("//div[2]/div/button").click()  # 点击获取验证码
        time.sleep(1)
        self.driver.find_element_by_xpath("//div[2]/div/input").send_keys("asdfasdf")  # 输入验证码
        self.driver.find_element_by_xpath("//div[3]/button").click()  # 点击确定
        time.sleep(1)
        self.driver.find_element_by_xpath("//li/a").click()    # 进入交易页面

    def LimitBuyOrder(self, price, size):
        u"""价格和数量参数化"""
        self.driver.find_element_by_xpath("//input").send_keys(price)    # 输入价格
        self.driver.find_element_by_xpath("//div[3]/input").send_keys(size)     # 输入数量
        self.driver.find_element_by_xpath("//div[2]/div/button").click()           # 点击买入
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

    def test10(self):
        u"""下限价委托多单，查看委托保证金"""
        self.driver.find_element_by_css_selector(".form-control:nth-child(1)").send_keys(10)  # 杠杆输入10x
        self.driver.find_element_by_xpath("//div[3]/div[2]/div").click()
        self.LimitBuyOrder(3500, 1000)
        message = self.driver.find_element_by_xpath("//span/div/div/div/div/div").text  # 创建成功
        self.assertTrue(message)
        print (u"弹出提示信息：%s" % message)  # 断言实际结果与期望结果一致
        time.sleep(1)

        self.driver.get("https://test.xjonathan.me/wallet/balance")  # 进入我的资产页面
        time.sleep(1)
        result = self.driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div[2]/div/div[3]/div/div/table/tbody/tr[5]/td[2]").text
        order_margin = "0.029 BTC"  # 1000 / 3500 * (0.1 + 2 * 0.00075) = 0.029
        self.assertEqual(result, order_margin)  # 断言实际结果与期望结果一致
        print (u"委托保证金：%s" % result)
        time.sleep(1)

    def test11(self):
        u"""下多笔限价委托多单，查看委托保证金"""
        self.driver.find_element_by_css_selector(".form-control:nth-child(1)").send_keys(10)  # 杠杆输入10x
        self.driver.find_element_by_xpath("//div[3]/div[2]/div").click()
        self.LimitBuyOrder(3499, 1000)
        message = self.driver.find_element_by_xpath("//span/div/div/div/div/div").text
        self.assertTrue(message)
        print (u"弹出提示信息：%s" % message)  # 断言实际结果与期望结果一致
        time.sleep(1)

        self.driver.get("https://test.xjonathan.me/wallet/balance")  # 进入我的资产页面
        time.sleep(1)
        result = self.driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div[2]/div/div[3]/div/div/table/tbody/tr[5]/td[2]").text
        order_margin = "0.05772256 BTC"
        # 1000 / 3500 * (0.1 - 0.00025 + 0.00075) = 0.02871428
        # 1000 / 3499 * (0.1 + 2 * 0.00075) = 0.02900828
        # 下多个订单时，之前同方向未成交的订单应以Maker Fee作为Entry Fee进行计算：0.02871428 + 0.02900828 = 0.05772256)
        self.assertEqual(result, order_margin)  # 断言实际结果与期望结果一致
        print (u"委托保证金：%s" % result)
        print (u"计算过程：\n\t 1000 / 3500 * (0.1 - 0.00025 + 0.00075) = 0.02871428 \n\t 1000 / 3499 * (0.1 + 2 * "
               u"0.00075) = 0.02900828 \n\t 0.02871428 + 0.02900828 = 0.05772256)")
        time.sleep(1)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()



