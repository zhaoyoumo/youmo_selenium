# -*-coding:utf-8-*-

import time
from selenium import webdriver
import unittest

__author__ = 'Youmo'


class SignIn(unittest.TestCase):
    u"""登录"""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://test.xjonathan.me/sign-in")
        self.driver.implicitly_wait(30)
        time.sleep(1)

    def SignIn(self, username, psw):
        u"""账号和密码参数化"""
        self.driver.find_element_by_id("account").send_keys(username)
        self.driver.find_element_by_id("password").send_keys(psw)
        self.driver.find_element_by_xpath("//div/div/button").click()
        time.sleep(1)

    def is_SignIn_success(self):
        u"""判断是否获取到登录账户名称"""
        try:
            text = self.driver.find_element_by_xpath("//li/div").text
            print text
            return True
        except:
            return False

    def test01(self):
        u"""正确账户，正确密码"""
        self.SignIn("zhaoyoumo@outlook.com", "Abcd1234**")  # 调用登录方法
        text = self.driver.find_element_by_xpath("//li/div").text  # 获取登录后的账号名称
        print text
        self.assertEqual(text, "zha******@outlook.com")  # 断言实际结果与期望结果一致
        print u"登录成功！"

    def test02(self):
        u"""正确账户，错误密码"""
        self.SignIn("zhaoyoumo@outlook.com", "**dddd")  # 调用登录方法
        error_message = self.driver.find_element_by_xpath("//span/div/div/div/div/div").text  # 获取错误提示
        self.assertTrue(error_message)  # 断言实际结果与期望结果一致
        print u"弹出错误提示：%s" % error_message

    def test03(self):
        u"""错误账户，错误密码"""
        self.SignIn("123@qq.com", "**dddd")  # 调用登录方法
        error_message = self.driver.find_element_by_xpath("//span/div/div/div/div/div").text  # 获取错误提示
        self.assertTrue(error_message)  # 断言实际结果与期望结果一致
        print u"弹出错误提示：%s" % error_message

    def test04(self):
        u"""邮箱号为空"""
        self.SignIn("", "Abcd1234**")
        error_message = self.driver.find_element_by_xpath("//form/div/div/span").text
        self.assertTrue(error_message)
        print u"弹出错误提示：%s" % error_message

    def test05(self):
        u"""密码为空"""
        self.SignIn("zhaoyoumo@outlook.com", "")
        error_message = self.driver.find_element_by_xpath("//div[2]/div/span").text
        self.assertTrue(error_message)
        print u'弹出错误提示：%s' % error_message

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
