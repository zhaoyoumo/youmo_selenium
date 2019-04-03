# -*-coding:utf-8-*-

import time
from selenium import webdriver
import unittest

__author__ = 'Youmo'


class SignIn(unittest.TestCase):
    u"登录"

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://test.xjonathan.me/sign-in")
        self.driver.implicitly_wait(30)
        time.sleep(1)

    def SignIn(self, username, psw):
        u'''账号和密码参数化'''
        self.driver.find_element_by_id("account").send_keys(username)
        self.driver.find_element_by_id("password").send_keys(psw)
        self.driver.find_element_by_xpath("//div/div/button").click()
        time.sleep(3)

    def is_SignIn_sucess(self):
        u'''判断是否获取到登录账户名称'''
        try:
            text = self.driver.find_element_by_xpath("//li/div").text
            print text
            return True
        except:
            return False

    def test_01(self):
        u'''正确账户，正确密码'''
        self.SignIn("zhaoyoumo@outlook.com", "Abcd1234**")  # 调用登录方法
        # 获取登录后的账号名称
        text = self.driver.find_element_by_xpath("//li/div").text
        print text
        # 断言实际结果与期望结果一致
        self.assertEqual(text, "zha******@outlook.com")
        print u"登录成功！"

    def test_02(self):
        u'''正确账户，错误密码'''
        self.SignIn("123@qq.com", "**dddd")  # 调用登录方法
        # 获取错误提示
        error_message = self.driver.find_element_by_xpath("//span/div/div/div/div/div").text
        # 断言实际结果与期望结果一致
        self.assertTrue(error_message)
        print (u"弹出错误提示：%s" % error_message)


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()


# if account == driver.find_element_by_id("account").click():
#     driver.find_element_by_xpath("//div/div/button").click()
#     feedback_1 = driver.find_element_by_xpath("//form/div/div").text
#     print (u"获取到的提示：%s" % feedback_1)
#     if feedback_1 == u"请输入邮箱/手机号":
#         print u"登录失败"
#     else:
#         print u"登录成功"
#         time.sleep(1)
#
# if account == driver.find_element_by_id("account").send_keys("10000000000"):
#     print u"输入错误的账户"
#     driver.find_element_by_xpath("//div/div/button").click()
#     feedback_2 = driver.find_element_by_id("password").text
#     print (u"获取到的提示：%s" % feedback_2)
#     if feedback_2 == u"输入您的登录密码":
#         print u"密码输入为空，登录失败"
#     else:
#         print u"登录成功"
#         time.sleep(1)


