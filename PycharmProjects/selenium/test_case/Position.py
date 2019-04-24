# -*-coding:utf-8-*-
import time
import unittest

from selenium import webdriver

__author__ = 'Youmo'


class Position(unittest.TestCase):
    u"""进入交易页面"""

    def setUp(self):
        u"""登录"""
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://test.xjonathan.me/sign-in")  # 进入登录页面
        self.driver.implicitly_wait(30)
        time.sleep(1)

    def LimitBuyOrder(self, price, size):
        u"""限价买单"""
        self.driver.find_element_by_xpath("//div[2]/input").send_keys(price)  # 输入价格
        self.driver.find_element_by_xpath("//div[3]/input").send_keys(size)  # 输入数量
        self.driver.find_element_by_xpath("//div[2]/div/button").click()  # 点击买入
        time.sleep(1)

    def LimitSellOrder(self, price, size):
        u"""限价卖单"""
        self.driver.find_element_by_xpath("//div[2]/input").send_keys(price)  # 输入价格
        self.driver.find_element_by_xpath("//div[3]/input").send_keys(size)  # 输入数量
        self.driver.find_element_by_xpath("//div[2]/button").click()  # 点击卖出
        time.sleep(1)

    def test01(self):
        u"""撮合成功，查看用户B（开空）的仓位"""
        print '----------Test01 Start----------'
        self.driver.find_element_by_xpath("//input[@id='account']").send_keys("zhaoyoumo@outlook.com")  # 输入用户名
        self.driver.find_element_by_xpath("//input[@id='password']").send_keys("Abcd1234**")  # 输入密码
        self.driver.find_element_by_xpath("//div/div/button").click()  # 登录用户A
        time.sleep(1)
        self.driver.get("https://test.xjonathan.me/trade")  # 进入交易页面
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_css_selector(".form-control:nth-child(1)").send_keys(10)  # 杠杆输入10x
        self.driver.find_element_by_xpath("//div[3]/div[2]/div").click()
        self.LimitBuyOrder(6000, 1000)
        message = self.driver.find_element_by_xpath("//span/div/div/div/div/div").text  # 买单创建成功
        self.assertTrue(message)
        print message
        time.sleep(1)

        self.driver.get("https://test.xjonathan.me/sign-in")
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath("//input[@id='account']").send_keys("zspkoliver@hotmail.com")  # 输入用户名
        self.driver.find_element_by_xpath("//input[@id='password']").send_keys("Abcd1234**")  # 输入密码
        self.driver.find_element_by_xpath("//div/div/button").click()  # 登录用户B
        time.sleep(1)
        self.driver.get("https://test.xjonathan.me/trade")  # 进入交易页面
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_css_selector(".form-control:nth-child(1)").send_keys(10)  # 杠杆输入10x
        self.driver.find_element_by_xpath("//div[3]/div[2]/div").click()
        self.LimitSellOrder(6000, 3000)
        message = self.driver.find_element_by_xpath("//span/div/div/div/div/div").text  # 卖单创建成功
        self.assertTrue(message)
        print message
        time.sleep(1)

        self.driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div[3]/div/div/ul/li/a/span").click()  # 用户B 进入仓位
        output_symbol = self.driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div[3]/div/div/div/div/table/tbody/tr/td").text  # 合约
        self.assertTrue(output_symbol)
        print u"合约：%s" % output_symbol

        output_quantity = self.driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div[4]/div/div/div/div/table/tbody/tr/td[2]").text  # 持仓数量
        input_quantity = "-1000"
        self.assertEqual(output_quantity, input_quantity)
        print u"持仓数量：%s" % output_quantity

        output_entryPrice = self.driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div[4]/div/div/div/div/table/tbody/tr/td[3]").text  # 开仓价格
        input_entryPrice = "6000"
        self.assertEqual(output_entryPrice, input_entryPrice)
        print u"开仓价格：%s" % output_entryPrice
        print u"计算过程：\n\t (|1000|+|1000|) / (|6000|/6000+|1000|/6000) = 6000"

        ouyput_liquidationPrice = self.driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div[4]/div/div/div/div/table/tbody/tr/td[4]").text  # 强平价格
        input_liquidationPrice = "6629.5"
        self.assertEqual(ouyput_liquidationPrice, input_liquidationPrice)
        print u"强平价格：%s" % ouyput_liquidationPrice
        print u"计算过程：\n\t 6000/（1 - 1/10 - 0.5% - 0.00000001）= 6629.5"

        output_margin = self.driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div[4]/div/div/div/div/table/tbody/tr/td[5]").text  # 保证金
        input_margin = "0.01679166"
        self.assertEqual(output_margin, input_margin)
        print u"保证金：%s" % output_margin
        print u"计算过程：\n\t（1000/6000）x（1/10 + 0.00075）+ 0 = 0.01679166"

        output_ROM = self.driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div[4]/div/div/div/div/table/tbody/tr/td[6]").text  # 回报率
        input_ROM = "0.00000000"
        self.assertEqual(output_ROM, input_ROM)
        print u"回报率：%s" % output_ROM
        print u"计算过程：\n\t 0 /（0.01679166 - 0) = 0"

        output_unrealisedPNL = self.driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div[4]/div/div/div/div/table/tbody/tr/td[7]").text  # 未实现盈亏
        input_unrealisedPNL = "0"
        self.assertEqual(output_unrealisedPNL, input_unrealisedPNL)
        print u"未实现盈亏：%s" % output_unrealisedPNL
        print u"计算过程：\n\t（1000/mark price)-(1000/6000) = ?"

        output_realisedPNL = self.driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div[4]/div/div/div/div/table/tbody/tr/td[8]").text  # 已实现盈亏
        input_realisedPNL = "-0.00012432"
        self.assertEqual(output_realisedPNL, input_realisedPNL)
        print u"已实现盈亏：%s" % output_realisedPNL
        print '----------Test01 Passed----------'

    def test02(self):
        u"""撮合成功，查看用户A（开多）的仓位"""
        print '----------Test02 Start----------'
        self.driver.find_element_by_xpath("//input[@id='account']").send_keys("zhaoyoumo@outlook.com")  # 输入用户名
        self.driver.find_element_by_xpath("//input[@id='password']").send_keys("Abcd1234**")  # 输入密码
        self.driver.find_element_by_xpath("//div/div/button").click()  # 登录用户A
        time.sleep(1)
        self.driver.get("https://test.xjonathan.me/trade")  # 用户A 进入交易页面
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div[3]/div/div/ul/li/a/span").click()  # 用户A 进入仓位
        output_symbol = self.driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div[3]/div/div/div/div/table/tbody/tr/td").text  # 合约
        self.assertTrue(output_symbol)
        print u"合约：%s" % output_symbol

        output_quantity = self.driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div[4]/div/div/div/div/table/tbody/tr/td[2]").text  # 持仓数量
        input_quantity = "1000"
        self.assertEqual(output_quantity, input_quantity)
        print u"持仓数量：%s" % output_quantity

        output_entryPrice = self.driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div[4]/div/div/div/div/table/tbody/tr/td[3]").text  # 开仓价格
        input_entryPrice = "6000"
        self.assertEqual(output_entryPrice, input_entryPrice)
        print u"开仓价格：%s" % output_entryPrice
        print u"计算过程：\n\t (|1000|+|1000|) / (|6000|/6000+|1000|/6000) = 6000"

        ouyput_liquidationPrice = self.driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div[4]/div/div/div/div/table/tbody/tr/td[4]").text  # 强平价格
        input_liquidationPrice = "5479.5"
        self.assertEqual(ouyput_liquidationPrice, input_liquidationPrice)
        print u"强平价格：%s" % ouyput_liquidationPrice
        print u"计算过程：\n\t 6000/（1+1/10-0.005-0.00000001）= 5479.5"

        output_margin = self.driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div[4]/div/div/div/div/table/tbody/tr/td[5]").text  # 保证金
        input_margin = "0.01679166"
        self.assertEqual(output_margin, input_margin)
        print u"保证金：%s" % output_margin
        print u"计算过程：\n\t（1000/6000）x（1/10+0.00075）+ 0 = 0.01679166"

        output_ROM = self.driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div[4]/div/div/div/div/table/tbody/tr/td[6]").text  # 回报率
        input_ROM = "0.00000000"
        self.assertEqual(output_ROM, input_ROM)
        print u"回报率：%s" % output_ROM
        print u"计算过程：\n\t 0 /（0.01679166 - 0) = 0"

        output_unrealisedPNL = self.driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div[4]/div/div/div/div/table/tbody/tr/td[7]").text  # 未实现盈亏
        input_unrealisedPNL = "0"
        self.assertEqual(output_unrealisedPNL, input_unrealisedPNL)
        print u"未实现盈亏：%s" % output_unrealisedPNL
        print u"计算过程：\n\t（1000/mark price)-(1000/6000) = ?"

        output_realisedPNL = self.driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div[4]/div/div/div/div/table/tbody/tr/td[8]").text  # 已实现盈亏
        input_realisedPNL = "0.00003758"
        self.assertEqual(output_realisedPNL, input_realisedPNL)
        print u"已实现盈亏：%s" % output_realisedPNL
        print '----------Test02 Passed----------'

    def test03(self):
        u"""追加仓位，查看用户A（开多）的仓位"""
        print '----------Test03 Start----------'
        self.driver.get("https://test.xjonathan.me/trade")  # 用户A 进入交易页面
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_css_selector(".form-control:nth-child(1)").send_keys(10)  # 杠杆输入10x
        self.driver.find_element_by_xpath("//div[3]/div[2]/div").click()
        self.LimitSellOrder(6000, 3000)
        message = self.driver.find_element_by_xpath("//span/div/div/div/div/div").text  # 买单创建成功
        self.assertTrue(message)
        print u"追加仓位：%s " % message
        time.sleep(1)
        self.driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div[3]/div/div/ul/li/a/span").click()  # 用户A 进入仓位
        output_symbol = self.driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div[3]/div/div/div/div/table/tbody/tr/td").text  # 合约
        self.assertTrue(output_symbol)
        print u"合约：%s" % output_symbol

        output_quantity = self.driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div[4]/div/div/div/div/table/tbody/tr/td[2]").text  # 持仓数量
        input_quantity = "2000"
        self.assertEqual(output_quantity, input_quantity)
        print u"持仓数量：%s" % output_quantity

        output_entryPrice = self.driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div[4]/div/div/div/div/table/tbody/tr/td[3]").text  # 开仓价格
        input_entryPrice = "6000"
        self.assertEqual(output_entryPrice, input_entryPrice)
        print u"开仓价格：%s" % output_entryPrice
        print u"计算过程：\n\t (|1000|+|1000|) / (|6000|/6000+|1000|/6000) = 6000"

        ouyput_liquidationPrice = self.driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div[4]/div/div/div/div/table/tbody/tr/td[4]").text  # 强平价格
        input_liquidationPrice = "5479.5"
        self.assertEqual(ouyput_liquidationPrice, input_liquidationPrice)
        print u"强平价格：%s" % ouyput_liquidationPrice
        print u"计算过程：\n\t 6000/（1+1/10-0.5%-0.00000001）= 5479.5"

        output_margin = self.driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div[4]/div/div/div/div/table/tbody/tr/td[5]").text  # 保证金
        input_margin = "0.03358332"
        self.assertEqual(output_margin, input_margin)
        print u"保证金：%s" % output_margin
        print u"计算过程：\n\t（1000/6000）x（1/10+0.00075）+ 0 = 0.01679166 " \
              u"\n\t （1000/6000）x（1/10+0.00075）+ 0 = 0.01679166 " \
              u"\n\t 0.01679166 + 0.01679166 = 0.03358332"

        output_ROM = self.driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div[4]/div/div/div/div/table/tbody/tr/td[6]").text  # 回报率
        input_ROM = "0.00000000"
        self.assertEqual(output_ROM, input_ROM)
        print u"回报率：%s" % output_ROM
        print u"计算过程：\n\t 0 /（0.03358332 - 0) = 0"

        output_unrealisedPNL = self.driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div[4]/div/div/div/div/table/tbody/tr/td[7]").text  # 未实现盈亏
        input_unrealisedPNL = "0"
        self.assertEqual(output_unrealisedPNL, input_unrealisedPNL)
        print u"未实现盈亏：%s" % output_unrealisedPNL
        print u"计算过程：\n\t（1000/mark price)-(1000/6000) = ?"

        output_realisedPNL = self.driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div[4]/div/div/div/div/table/tbody/tr/td[8]").text  # 已实现盈亏
        input_realisedPNL = "-0.0000926"
        self.assertEqual(output_realisedPNL, input_realisedPNL)
        print u"已实现盈亏：%s" % output_realisedPNL
        print '----------Test03 Passed----------'

    def test04(self):
        u"""追加仓位，查看用户B（开空）的仓位"""
        print '----------Test04 Start----------'
        self.driver.find_element_by_xpath("//input[@id='account']").send_keys("zspkoliver@hotmail.com")  # 输入用户名
        self.driver.find_element_by_xpath("//input[@id='password']").send_keys("Abcd1234**")  # 输入密码
        self.driver.find_element_by_xpath("//div/div/button").click()  # 登录用户B
        self.driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div[3]/div/div/ul/li/a/span").click()  # 用户B 进入仓位
        output_symbol = self.driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div[3]/div/div/div/div/table/tbody/tr/td").text  # 合约
        self.assertTrue(output_symbol)
        print u"合约：%s" % output_symbol

        output_quantity = self.driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div[4]/div/div/div/div/table/tbody/tr/td[2]").text  # 持仓数量
        input_quantity = "-2000"
        self.assertEqual(output_quantity, input_quantity)
        print u"持仓数量：%s" % output_quantity

        output_entryPrice = self.driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div[4]/div/div/div/div/table/tbody/tr/td[3]").text  # 开仓价格
        input_entryPrice = "6000"
        self.assertEqual(output_entryPrice, input_entryPrice)
        print u"开仓价格：%s" % output_entryPrice
        print u"计算过程：\n\t (|1000|+|1000|) / (|6000|/6000+|1000|/6000) = 6000"

        ouyput_liquidationPrice = self.driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div[4]/div/div/div/div/table/tbody/tr/td[4]").text  # 强平价格
        input_liquidationPrice = "6629.5"
        self.assertEqual(ouyput_liquidationPrice, input_liquidationPrice)
        print u"强平价格：%s" % ouyput_liquidationPrice
        print u"计算过程：\n\t 6000/（1 - 1/10 - 0.5% - 0.00000001）= 6629.5"

        output_margin = self.driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div[4]/div/div/div/div/table/tbody/tr/td[5]").text  # 保证金
        input_margin = "0.03358332"
        self.assertEqual(output_margin, input_margin)
        print u"保证金：%s" % output_margin
        print u"计算过程：\n\t（1000/6000）x（1/10 + 0.00075）+ 0 = 0.01679166 " \
              u"\n\t（1000/6000）x（1/10 + 0.00075）+ 0 = 0.01679166 " \
              u"\n\t 0.01679166 + 0.01679166 = 0.03358332 "

        output_ROM = self.driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div[4]/div/div/div/div/table/tbody/tr/td[6]").text  # 回报率
        input_ROM = "0.00000000"
        self.assertEqual(output_ROM, input_ROM)
        print u"回报率：%s" % output_ROM
        print u"计算过程：\n\t 0 /（0.01679166 - 0) = 0"

        output_unrealisedPNL = self.driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div[4]/div/div/div/div/table/tbody/tr/td[7]").text  # 未实现盈亏
        input_unrealisedPNL = "0"
        self.assertEqual(output_unrealisedPNL, input_unrealisedPNL)
        print u"未实现盈亏：%s" % output_unrealisedPNL
        print u"计算过程：\n\t（1000/mark price)-(1000/6000) = ?"

        output_realisedPNL = self.driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div[4]/div/div/div/div/table/tbody/tr/td[8]").text  # 已实现盈亏
        input_realisedPNL = "-0.00007338"
        self.assertEqual(output_realisedPNL, input_realisedPNL)
        print u"已实现盈亏：%s" % output_realisedPNL
        print '----------Test04 Passed----------'

    # def test(self):
    #     u"平仓操作"

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
