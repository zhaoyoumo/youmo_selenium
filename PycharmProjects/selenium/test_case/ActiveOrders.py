# -*-coding:utf-8-*-
import unittest

import time
from selenium import webdriver

__author__ = 'Youmo'


class ActiveOrder(unittest.TestCase):
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

    def test01(self):
        u"""下限价委托多单，查看当前委托列表"""
        print '----------Test01 Start----------'
        self.driver.find_element_by_css_selector(".form-control:nth-child(1)").send_keys(10)  # 杠杆输入10x
        self.driver.find_element_by_xpath("//div[3]/div[2]/div").click()
        self.LimitBuyOrder(3500, 1000)
        message = self.driver.find_element_by_xpath("//span/div/div/div/div/div").text  # 创建成功
        self.assertTrue(message)
        print (u"弹出提示信息：%s" % message)  # 断言实际结果与期望结果一致
        time.sleep(1)

        self.driver.find_element_by_xpath("//div[3]/div/div/ul/li[2]/a/span").click()  # 点击当前委托
        output_price = self.driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div[3]/div/div/div/div[2]/table/tbody/tr/td[2]").text  # 委托价格
        input_price = "3500"
        self.assertEqual(output_price, input_price)  # 断言实际结果与期望结果一致
        print (u"委托价格：%s" % output_price)
        output_size = self.driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div[3]/div/div/div/div[2]/table/tbody/tr/td[3]").text  # 委托数量
        input_size = "1000"
        self.assertEqual(output_size, input_size)  # 断言实际结果与期望结果一致
        print (u"委托数量：%s" % output_size)
        self.driver.find_element_by_xpath()  # 成交数量
        self.driver.find_element_by_xpath()  # 委托价值
        self.driver.find_element_by_xpath()  # 成交价格
        self.driver.find_element_by_xpath()  # 状态
        self.driver.find_element_by_xpath()  # 时间

        print '----------Test01 Passed---------'

    def test02(self):
        u"""下限价空单，查看当前委托列表"""
        print '----------Test02 Start----------'
        self.driver.find_element_by_css_selector(".form-control:nth-child(1)").send_keys(10)
        self.driver.find_element_by_xpath("//div[3]/div[2]/div").click()
        self.LimitSellOrder(3500, 1000)
        message = self.driver.find_element_by_xpath("//span/div/div/div/div/div").text
        self.assertTrue(message)
        print (u"弹出提示信息：%s" % message)
        time.sleep(1)

        self.driver.find_element_by_xpath("//div[3]/div/div/ul/li[2]/a/span").click()  # 点击当前委托
        output_price = self.driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div[3]/div/div/div/div[2]/table/tbody/tr[2]/td[2]").text
        input_price = "3500"
        self.assertEqual(output_price, input_price)
        print (u"委托价格：%s" % output_price)
        output_size = self.driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div[3]/div/div/div/div[2]/table/tbody/tr/td[3]").text
        input_size = "1000"
        self.assertEqual(output_size, input_size)
        print (u"委托数量：%s" % output_size)
        print '----------Test02 Passed----------'

    # def test03(self):
    #     u"""取消当前委托"""
    #     print '----------Test03 Start----------'
    #     self.driver.get("https://test.xjonathan.me/trade")
    #     self.driver.implicitly_wait(30)
    #     self.driver.find_element_by_xpath("//div[3]/div/div/ul/li[2]/a/span").click()
    #     self.driver.find_element_by_xpath("//td[9]/button/span").click()  # 点击取消按钮
    #     print (u'当前委托单已撤单')
    #     print '----------Test03 Passed----------'

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
