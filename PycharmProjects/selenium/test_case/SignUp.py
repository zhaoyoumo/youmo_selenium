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
        self.driver.get("https://test.xjonathan.me/sign-up")
        self.driver.implicitly_wait(30)
        time.sleep(1)

    def test01(self):
        u"""邮箱为空"""
        self.driver.find_element_by_xpath("//input[@type='email']").click()
        self.driver.find_element_by_id("password").send_keys("Abcd1234**")
        self.driver.find_element_by_id("rePassword").send_keys("Abcd1234**")
        self.driver.find_element_by_xpath("//div[@id='root']/div/div[2]/div/div/div/div/button/span").click()
        text = self.driver.find_element_by_css_selector(".due-message-text").text
        self.assertTrue(text)
        print u'弹出错误提示：%s' % text

    def test02(self):
        u"""密码为空"""
        self.driver.find_element_by_xpath("//input[@type='email']").send_keys("abc1234@qq.com")
        self.driver.find_element_by_id("password").click()
        self.driver.find_element_by_id("rePassword").send_keys("Abcd1234**")
        self.driver.find_element_by_xpath("//div[@id='root']/div/div[2]/div/div/div/div/button/span").click()
        text = self.driver.find_element_by_css_selector(".due-message-text").text
        self.assertTrue(text)
        print (u'弹出错误提示：%s' % text)

    def test03(self):
        u"""密码为纯数字"""
        self.driver.find_element_by_xpath("//input[@type='email']").send_keys("abc1234@qq.com")
        self.driver.find_element_by_id("password").send_keys("1234567890")
        self.driver.find_element_by_id("rePassword").send_keys("Abcd1234**")
        self.driver.find_element_by_xpath("//div[@id='root']/div/div[2]/div/div/div/div/button/span").click()
        text = self.driver.find_element_by_css_selector(".due-message-text").text
        self.assertTrue(text)
        print (u'弹出错误提示：%s' % text)

    def test04(self):
        u"""密码为纯字母"""
        self.driver.find_element_by_xpath("//input[@type='email']").send_keys("abc1234@qq.com")
        self.driver.find_element_by_id("password").send_keys("abcdefghijk")
        self.driver.find_element_by_id("rePassword").send_keys("abcdefghijk")
        self.driver.find_element_by_xpath("//div[@id='root']/div/div[2]/div/div/div/div/button/span").click()
        text = self.driver.find_element_by_css_selector(".due-message-text").text
        self.assertTrue(text)
        print (u'弹出错误提示：%s' % text)

    def test05(self):
        u"""密码为纯符号"""
        self.driver.find_element_by_xpath("//input[@type='email']").send_keys("abc1234@qq.com")
        self.driver.find_element_by_id("password").send_keys("@@@@@@@@@@")
        self.driver.find_element_by_id("rePassword").send_keys("@@@@@@@@@@")
        self.driver.find_element_by_xpath("//div[@id='root']/div/div[2]/div/div/div/div/button/span").click()
        text = self.driver.find_element_by_css_selector(".due-message-text").text
        self.assertTrue(text)
        print (u'弹出错误提示：%s' % text)

    def test06(self):
        u"""密码为数字字母组合"""
        self.driver.find_element_by_xpath("//input[@type='email']").send_keys("abc1234@qq.com")
        self.driver.find_element_by_id("password").send_keys("1234abcdef")
        self.driver.find_element_by_id("rePassword").send_keys("1234abcdef")
        self.driver.find_element_by_xpath("//div[@id='root']/div/div[2]/div/div/div/div/button/span").click()
        text = self.driver.find_element_by_css_selector(".due-message-text").text
        self.assertTrue(text)
        print (u'弹出错误提示：%s' % text)

    def test07(self):
        u"""密码为数字符号组合"""
        self.driver.find_element_by_xpath("//input[@type='email']").send_keys("abc1234@qq.com")
        self.driver.find_element_by_id("password").send_keys("1234*****")
        self.driver.find_element_by_id("rePassword").send_keys("1234*****")
        self.driver.find_element_by_xpath("//div[@id='root']/div/div[2]/div/div/div/div/button/span").click()
        text = self.driver.find_element_by_css_selector(".due-message-text").text
        self.assertTrue(text)
        print (u'弹出错误提示：%s' % text)

    def test08(self):
        u"""密码为字母符号组合"""
        self.driver.find_element_by_xpath("//input[@type='email']").send_keys("abc1234@qq.com")
        self.driver.find_element_by_id("password").send_keys("abcd*****")
        self.driver.find_element_by_id("rePassword").send_keys("abcd*****")
        self.driver.find_element_by_xpath("//div[@id='root']/div/div[2]/div/div/div/div/button/span").click()
        text = self.driver.find_element_by_css_selector(".due-message-text").text
        self.assertTrue(text)
        print (u'弹出错误提示：%s' % text)

    def test09(self):
        u"""密码为7位"""
        self.driver.find_element_by_xpath("//input[@type='email']").send_keys("abc1234@qq.com")
        self.driver.find_element_by_id("password").send_keys("Acbd12*")
        self.driver.find_element_by_id("rePassword").send_keys("Acbd12*")
        self.driver.find_element_by_xpath("//div[@id='root']/div/div[2]/div/div/div/div/button/span").click()
        text = self.driver.find_element_by_css_selector(".due-message-text").text
        self.assertTrue(text)
        print (u'弹出错误提示：%s' % text)

    def test10(self):
        u"""密码为21位"""
        self.driver.find_element_by_xpath("//input[@type='email']").send_keys("abc1234@qq.com")
        self.driver.find_element_by_id("password").send_keys("Aaaaaaaaaa99999*****0")
        self.driver.find_element_by_id("rePassword").send_keys("Aaaaaaaaaa99999*****0")
        self.driver.find_element_by_xpath("//div[@id='root']/div/div[2]/div/div/div/div/button/span").click()
        text = self.driver.find_element_by_css_selector(".due-message-text").text
        self.assertTrue(text)
        print (u'弹出错误提示：%s' % text)

    def test11(self):
        u"""确认密码为空"""
        self.driver.find_element_by_xpath("//input[@type='email']").send_keys("abc1234@qq.com")
        self.driver.find_element_by_id("password").send_keys("Abcd1234**")
        self.driver.find_element_by_id("rePassword").click()
        self.driver.find_element_by_xpath("//div[@id='root']/div/div[2]/div/div/div/div/button/span").click()
        text = self.driver.find_element_by_css_selector(".due-message-text").text
        self.assertTrue(text)
        print (u'弹出错误提示：%s' % text)

    def test12(self):
        u"""确认密码输入错误"""
        self.driver.find_element_by_xpath("//input[@type='email']").send_keys("abc1234@qq.com")
        self.driver.find_element_by_id("password").send_keys("Abcd1234**")
        self.driver.find_element_by_id("rePassword").send_keys("1234Abcd&&")
        self.driver.find_element_by_xpath("//div[@id='root']/div/div[2]/div/div/div/div/button/span").click()
        text = self.driver.find_element_by_css_selector(".due-message-text").text
        self.assertTrue(text)
        print (u'弹出错误提示：%s' % text)

    def test13(self):
        u"""输入错误邀请码"""
        self.driver.find_element_by_xpath("//input[@type='email']").send_keys("abc1234@qq.com")
        self.driver.find_element_by_id("password").send_keys("Abcd1234**")
        self.driver.find_element_by_id("rePassword").send_keys("Abcd1234**")
        self.driver.find_element_by_xpath("//div[@id='root']/div/div[2]/div/div/div/div/form/div[5]/input").send_keys(
            "AAAAAA")
        self.driver.find_element_by_xpath("//div[@id='root']/div/div[2]/div/div/div/div/button/span").click()
        text = self.driver.find_element_by_css_selector(".due-message-text").text
        self.assertTrue(text)
        print (u'弹出错误提示：%s' % text)

    def test14(self):
        u"""未勾选注册协议"""
        self.driver.find_element_by_xpath("//input[@type='email']").send_keys("abc1234@qq.com")
        self.driver.find_element_by_id("password").send_keys("Abcd1234**")
        self.driver.find_element_by_id("rePassword").send_keys("Abcd1234**")
        # self.driver.find_element_by_xpath(
        #     "//div[@id='root']/div/div[2]/div/div/div/div/form/div[6]/div/label").click()  # 勾选《注册协议》
        self.driver.find_element_by_xpath("//div[@id='root']/div/div[2]/div/div/div/div/button/span").click()
        text = self.driver.find_element_by_css_selector(".due-message-text").text
        self.assertTrue(text)
        print (u'弹出错误提示：%s' % text)

    def test15(self):
        u"""邮箱已注册"""
        self.driver.find_element_by_xpath("//input[@type='email']").send_keys("zhaoyomo@outlook.com")
        self.driver.find_element_by_id("password").send_keys("Abcd1234**")
        self.driver.find_element_by_id("rePassword").send_keys("Abcd1234**")
        self.driver.find_element_by_xpath("//div[@id='root']/div/div[2]/div/div/div/div/button/span").click()
        text = self.driver.find_element_by_css_selector(".due-message-text").text
        self.assertTrue(text)
        print u'弹出错误提示：%s' % text

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
