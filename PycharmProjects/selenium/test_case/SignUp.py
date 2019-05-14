# -*-coding:utf-8-*-
import time

from selenium import webdriver
import unittest

__author__ = 'Youmo'


class SignUp(unittest.TestCase):
    u"""注册"""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://test.xjonathan.me/register")
        self.driver.implicitly_wait(30)
        time.sleep(1)

    def test01(self):
        u"""邮箱为空"""
        print ('----------Test01 Start----------')
        self.driver.find_element_by_id("password").send_keys("Abcd1234**")
        self.driver.find_element_by_name("confirmedPassword").send_keys("Abcd1234**")
        self.driver.find_element_by_id("registerBtn").click()
        text = self.driver.find_element_by_css_selector(".due-message-text").text
        self.assertTrue(text)
        print (u'弹出错误提示：%s' % text)
        print ('----------Test01 Passed----------')

    def test02(self):
        u"""密码为空"""
        print ('----------Test02 Start----------')
        self.driver.find_element_by_name("email").send_keys("zhaoyoumo@outlook.com")
        self.driver.find_element_by_name("confirmedPassword").send_keys("Abcd1234**")
        self.driver.find_element_by_id("registerBtn").click()
        text = self.driver.find_element_by_css_selector(".due-message-text").text
        self.assertTrue(text)
        print (u'弹出错误提示：%s' % text)
        print ('----------Test02 Passed----------')

    def test03(self):
        u"""密码为纯数字"""
        print ('----------Test03 Start----------')
        self.driver.find_element_by_name("email").send_keys("zhaoyoumo@outlook.com")
        self.driver.find_element_by_id("password").send_keys("12345678")
        self.driver.find_element_by_name("confirmedPassword").send_keys("12345678")
        self.driver.find_element_by_id("registerBtn").click()
        text = self.driver.find_element_by_css_selector(".due-message-text").text
        self.assertTrue(text)
        print (u'弹出错误提示：%s' % text)
        print ('----------Test03 Passed----------')

    def test04(self):
        u"""密码为纯字母"""
        print ('----------Test04 Start----------')
        self.driver.find_element_by_name("email").send_keys("zhaoyoumo@outlook.com")
        self.driver.find_element_by_id("password").send_keys("abcdefghijk")
        self.driver.find_element_by_name("confirmedPassword").send_keys("abcdefghijk")
        self.driver.find_element_by_id("registerBtn").click()
        text = self.driver.find_element_by_css_selector(".due-message-text").text
        self.assertTrue(text)
        print (u'弹出错误提示：%s' % text)
        print ('----------Test04 Passed----------')

    def test05(self):
        u"""密码为纯符号"""
        print ('----------Test05 Start----------')
        self.driver.find_element_by_name("email").send_keys("zhaoyoumo@outlook.com")
        self.driver.find_element_by_id("password").send_keys("@@@@@@@@@@")
        self.driver.find_element_by_name("confirmedPassword").send_keys("@@@@@@@@@@")
        self.driver.find_element_by_id("registerBtn").click()
        text = self.driver.find_element_by_css_selector(".due-message-text").text
        self.assertTrue(text)
        print (u'弹出错误提示：%s' % text)
        print ('----------Test05 Passed----------')

    def test06(self):
        u"""密码为数字字母组合"""
        print ('----------Test06 Start----------')
        self.driver.find_element_by_name("email").send_keys("zhaoyoumo@outlook.com")
        self.driver.find_element_by_id("password").send_keys("1234abcdef")
        self.driver.find_element_by_name("confirmedPassword").send_keys("1234abcdef")
        self.driver.find_element_by_id("registerBtn").click()
        text = self.driver.find_element_by_css_selector(".due-message-text").text
        self.assertTrue(text)
        print (u'弹出错误提示：%s' % text)
        print ('----------Test06 Passed----------')

    def test07(self):
        u"""密码为数字符号组合"""
        print ('----------Test07 Start----------')
        self.driver.find_element_by_name("email").send_keys("zhaoyoumo@outlook.com")
        self.driver.find_element_by_id("password").send_keys("1234*****")
        self.driver.find_element_by_name("confirmedPassword").send_keys("1234*****")
        self.driver.find_element_by_id("registerBtn").click()
        text = self.driver.find_element_by_css_selector(".due-message-text").text
        self.assertTrue(text)
        print (u'弹出错误提示：%s' % text)
        print ('----------Test07 Passed----------')

    def test08(self):
        u"""密码为字母符号组合"""
        print ('----------Test08 Start----------')
        self.driver.find_element_by_name("email").send_keys("zhaoyoumo@outlook.com")
        self.driver.find_element_by_id("password").send_keys("abcd*****")
        self.driver.find_element_by_name("confirmedPassword").send_keys("abcd*****")
        self.driver.find_element_by_id("registerBtn").click()
        text = self.driver.find_element_by_css_selector(".due-message-text").text
        self.assertTrue(text)
        print (u'弹出错误提示：%s' % text)
        print ('----------Test08 Passed----------')

    def test09(self):
        u"""密码为7位"""
        print ('----------Test09 Start----------')
        self.driver.find_element_by_name("email").send_keys("zhaoyoumo@outlook.com")
        self.driver.find_element_by_id("password").send_keys("Acbd12*")
        self.driver.find_element_by_name("confirmedPassword").send_keys("Acbd12*")
        self.driver.find_element_by_id("registerBtn").click()
        text = self.driver.find_element_by_css_selector(".due-message-text").text
        self.assertTrue(text)
        print (u'弹出错误提示：%s' % text)
        print ('----------Test09 Passed----------')


    def test10(self):
        u"""密码为21位"""
        print ('----------Test10 Start----------')
        self.driver.find_element_by_name("email").send_keys("zhaoyoumo@outlook.com")
        self.driver.find_element_by_id("password").send_keys("Aaaaaaaaaa99999*****0")
        self.driver.find_element_by_name("confirmedPassword").send_keys("Aaaaaaaaaa99999*****0")
        self.driver.find_element_by_id("registerBtn").click()
        text = self.driver.find_element_by_css_selector(".due-message-text").text
        self.assertTrue(text)
        print (u'弹出错误提示：%s' % text)
        print ('----------Test10 Passed----------')

    def test11(self):
        u"""确认密码为空"""
        print ('----------Test11 Start----------')
        self.driver.find_element_by_name("email").send_keys("zhaoyoumo@outlook.com")
        self.driver.find_element_by_id("password").send_keys("Abcd1234**")
        self.driver.find_element_by_id("registerBtn").click()
        text = self.driver.find_element_by_css_selector(".due-message-text").text
        self.assertTrue(text)
        print (u'弹出错误提示：%s' % text)
        print ('----------Test11 Passed----------')
#
#    def test12(self):
#        u"""确认密码输入错误"""
#        self.driver.find_element_by_xpath("//input[@type='email']").send_keys("abc1234@qq.com")
#        self.driver.find_element_by_id("password").send_keys("Abcd1234**")
#        self.driver.find_element_by_id("rePassword").send_keys("1234Abcd&&")
#        self.driver.find_element_by_xpath("//div[@id='root']/div/div[2]/div/div/div/div/button/span").click()
#        text = self.driver.find_element_by_css_selector(".due-message-text").text
#        self.assertTrue(text)
#        print (u'弹出错误提示：%s' % text)
#
#    def test13(self):
#        u"""输入错误邀请码"""
#        self.driver.find_element_by_xpath("//input[@type='email']").send_keys("abc1234@qq.com")
#        self.driver.find_element_by_id("password").send_keys("Abcd1234**")
#        self.driver.find_element_by_id("rePassword").send_keys("Abcd1234**")
#        self.driver.find_element_by_xpath("//div[@id='root']/div/div[2]/div/div/div/div/form/div[5]/input").send_keys(
#            "AAAAAA")
#        self.driver.find_element_by_xpath("//div[@id='root']/div/div[2]/div/div/div/div/button/span").click()
#        text = self.driver.find_element_by_css_selector(".due-message-text").text
#        self.assertTrue(text)
#        print (u'弹出错误提示：%s' % text)
#
#    def test14(self):
#        u"""未勾选注册协议"""
#        self.driver.find_element_by_xpath("//input[@type='email']").send_keys("abc1234@qq.com")
#        self.driver.find_element_by_id("password").send_keys("Abcd1234**")
#        self.driver.find_element_by_id("rePassword").send_keys("Abcd1234**")
#        # self.driver.find_element_by_xpath(
#        #     "//div[@id='root']/div/div[2]/div/div/div/div/form/div[6]/div/label").click()  # 勾选《注册协议》
#        self.driver.find_element_by_xpath("//div[@id='root']/div/div[2]/div/div/div/div/button/span").click()
#        text = self.driver.find_element_by_css_selector(".due-message-text").text
#        self.assertTrue(text)
#        print (u'弹出错误提示：%s' % text)
#
#    def test15(self):
#        u"""邮箱已注册"""
#        self.driver.find_element_by_xpath("//input[@type='email']").send_keys("zhaoyomo@outlook.com")
#        self.driver.find_element_by_id("password").send_keys("Abcd1234**")
#        self.driver.find_element_by_id("rePassword").send_keys("Abcd1234**")
#        self.driver.find_element_by_xpath("//div[@id='root']/div/div[2]/div/div/div/div/button/span").click()
#        text = self.driver.find_element_by_css_selector(".due-message-text").text
#        self.assertTrue(text)
#        print (u'弹出错误提示：%s' % text)
#
#    def test16(self):
#        u"""邮箱错误"""
#        self.driver.find_element_by_xpath("//input[@type='email']").send_keys("zhaoyomo@.com")
#        self.driver.find_element_by_id("password").send_keys("Abcd1234**")
#        self.driver.find_element_by_id("rePassword").send_keys("Abcd1234**")
#        self.driver.find_element_by_xpath("//div[@id='root']/div/div[2]/div/div/div/div/button/span").click()
#        text = self.driver.find_element_by_css_selector(".due-message-text").text
#        self.assertTrue(text)
#        print (u'弹出错误提示：%s' % text)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
