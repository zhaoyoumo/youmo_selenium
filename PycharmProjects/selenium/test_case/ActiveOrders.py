# -*-coding:utf-8-*-
import unittest

import time
from selenium import webdriver

__author__ = 'Youmo'

class ActiveOrder(unittest.TestCase):
    u"""当前委托"""

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
        message = self.driver.find_element_by_xpath("//span/div/div/div/div/div").text  # 买单创建成功
        self.assertTrue(message)
        print message
        time.sleep(1)

        self.driver.find_element_by_xpath("//div[3]/div/div/ul/li[2]/a/span").click()  # 点击当前委托
        output_symbol = self.driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div[3]/div/div/div/div[2]/table/tbody/tr/td").text  # 合约
        input_symbol = "BTCUSD"
        self.assertEqual(output_symbol, input_symbol)
        print u"合约：%s" % output_symbol

        output_price = self.driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div[3]/div/div/div/div[2]/table/tbody/tr/td[2]").text  # 委托价格
        input_price = "3500"
        self.assertEqual(output_price, input_price)
        print u"委托价格：%s" % output_price

        output_size = self.driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div[3]/div/div/div/div[2]/table/tbody/tr/td[3]").text  # 委托数量
        input_size = "1000"
        self.assertEqual(output_size, input_size)
        print u"委托数量：%s" % output_size

        output_filled = self.driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div[3]/div/div/div/div[2]/table/tbody/tr/td[4]").text  # 成交数量
        input_filled = "0"
        self.assertEqual(output_filled, input_filled)
        print u"成交数量：%s" % output_filled

        output_orderValue = self.driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div[3]/div/div/div/div[2]/table/tbody/tr/td[5]").text  # 委托价值
        input_orderValue = "?"  # "0.28571428"
        self.assertEqual(output_orderValue, input_orderValue)
        print u"委托价值：%s" % output_orderValue

        output_fillPrice = self.driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div[3]/div/div/div/div[2]/table/tbody/tr/td[6]").text  # 成交价格
        input_fillPrice = "?"
        self.assertEqual(output_fillPrice, input_fillPrice)
        print u"成交价格：%s" % output_fillPrice

        output_status = self.driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div[3]/div/div/div/div[2]/table/tbody/tr/td[7]").text  # 状态
        input_status = "new"
        self.assertEqual(output_status, input_status)
        print u"状态：%s" % output_status

        output_time = self.driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div[3]/div/div/div/div[2]/table/tbody/tr/td[8]/div").text  # 时间
        self.assertTrue(output_time)
        print '----------Test01 Passed---------'

    def test02(self):
        u"""下限价空单，查看当前委托列表"""
        print '----------Test02 Start----------'
        self.driver.find_element_by_css_selector(".form-control:nth-child(1)").send_keys(10)  # 杠杆输入10x
        self.driver.find_element_by_xpath("//div[3]/div[2]/div").click()
        self.LimitSellOrder(4000, 1000)
        message = self.driver.find_element_by_xpath("//span/div/div/div/div/div").text  # 卖单创建成功
        self.assertTrue(message)
        print u"弹出提示信息：%s" % message
        time.sleep(1)

        self.driver.find_element_by_xpath("//div[3]/div/div/ul/li[2]/a/span").click()  # 点击当前委托
        output_symbol = self.driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div[3]/div/div/div/div[2]/table/tbody/tr[2]/td").text  # 合约
        input_symbol = "BTCUSD"
        self.assertEqual(output_symbol, input_symbol)
        print u"合约：%s" % output_symbol

        output_price = self.driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div[3]/div/div/div/div[2]/table/tbody/tr[2]/td[2]").text  # 委托价格
        input_price = "4000"
        self.assertEqual(output_price, input_price)
        print u"委托价格：%s" % output_price

        output_size = self.driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div[3]/div/div/div/div[2]/table/tbody/tr[2]/td[2]").text  # 委托数量
        input_size = "1000"
        self.assertEqual(output_size, input_size)
        print u"委托数量：%s" % output_size

        output_filled = self.driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div[3]/div/div/div/div[2]/table/tbody/tr[2]/td[4]").text  # 成交数量
        input_filled = "0"
        self.assertEqual(output_filled, input_filled)
        print u"成交数量：%s" % output_filled

        output_orderValue = self.driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div[3]/div/div/div/div[2]/table/tbody/tr[2]/td[5]").text  # 委托价值
        input_orderValue = "?"
        self.assertEqual(output_orderValue, input_orderValue)
        print u"委托价值：%s" % output_orderValue

        output_fillPrice = self.driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div[3]/div/div/div/div[2]/table/tbody/tr[2]/td[5]").text  # 成交价格
        input_fillPrice = "?"
        self.assertEqual(output_fillPrice, input_fillPrice)
        print u"成交价格：%s" % output_fillPrice

        output_status = self.driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div[3]/div/div/div/div[2]/table/tbody/tr[2]/td[7]").text  # 状态
        input_status = "new"
        self.assertEqual(output_status, input_status)
        print u"状态：%s" % output_status

        output_time = self.driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div[3]/div/div/div/div[2]/table/tbody/tr[2]/td[8]/div").text  # 时间
        self.assertTrue(output_time)
        print '----------Test02 Passed----------'

    def test03(self):
        u"""取消当前委托"""
        print '----------Test03 Start----------'
        self.driver.find_element_by_xpath("//div[3]/div/div/ul/li[2]/a/span").click()  # 进入当前委托
        self.driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div[3]/div/div/div/div[2]/table/tbody/tr/td[9]/button/span").click()  # 取消第一条
        self.driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div[3]/div/div/div/div[2]/table/tbody/tr[2]/td[9]/button/span")  # 取消第二条
        print (u'当前委托单已撤单')
        print '----------Test03 Passed----------'

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
