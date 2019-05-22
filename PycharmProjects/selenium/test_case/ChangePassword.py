# -*-coding:utf-8-*-

import time
from selenium import webdriver
import unittest

__author__ = 'Youmo'


class ChangePsw(unittest.TestCase):
    u"""修改密码"""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://test.xjonathan.me/login")
        self.driver.implicitly_wait(30)
        time.sleep(1)
        self.driver.find_element_by_id("account").send_keys("zhaoyoumo@outlook.com")
        self.driver.find_element_by_id("password").send_keys("Abcd1234**")
        self.driver.find_element_by_xpath("//div/div/button").click()  # 登录
        self.driver.find_element_by_xpath("//form/div/div/button").click()  # 选择验证方式
        self.driver.find_element_by_xpath("//div[2]/div/button").click()  # 点击获取验证码
        time.sleep(1)
        self.driver.find_element_by_xpath("//div[2]/div/input").send_keys("asdfasdf")  # 输入验证码
        self.driver.find_element_by_xpath("//div[3]/button").click()  # 点击确定
        time.sleep(1)
        self.driver.get("https://test.xjonathan.me/mine/change-password")  # 进入修改密码页面
        
    def test01(self):
        u"""旧密码为空"""
        self.driver.find_element_by_xpath("//div[2]/input").send_keys("Abcd1234**")    # 输入新密码
        self.driver.find_element_by_xpath("//div[3]/input").send_keys("Abcd1234**")    # 确认新密码
        self.driver.find_element_by_xpath("//div/div/button").click()    # 点击确认按钮
        text = self.driver.find_element_by_css_selector(".invalid-feedback > span").text    # 旧密码文本框下错误提示
        self.assertTrue(text)
        print(u'弹出提示信息：%s' % text)
        
    def test02(self):
        u"""新密码为空"""
        self.driver.find_element_by_xpath("//input").send_keys("Abcd1234**")    # 输入旧密码
        self.driver.find_element_by_xpath("//div[3]/input").send_keys("Abcd1234**")    # 确认新密码
        self.driver.find_element_by_xpath("//div/div/button").click()    # 点击确认按钮
        text = self.driver.find_element_by_css_selector(".form-group:nth-child(2) > .invalid-feedback").text    # 新密码文本框下错误提示
        self.assertTrue(text)
        print(u'弹出提示信息：%s' % text)
        
    def test03(self):
        u"""确认新密码为空"""
        self.driver.find_element_by_xpath("//input").send_keys("Abcd1234**")    # 输入旧密码
        self.driver.find_element_by_xpath("//div[2]/input").send_keys("Abcd1234**")    # 输入新密码
        self.driver.find_element_by_xpath("//div/div/button").click()    # 点击确认按钮
        text = self.driver.find_element_by_css_selector(".form-group:nth-child(2) > .invalid-feedback").text    # 确认新密码文本框下错误提示
        self.assertTrue(text)
        print(u'弹出提示信息：%s' % text)
        
    def test04(self):
        u"""旧密码错误"""
        self.driver.find_element_by_xpath("//div[2]/input").send_keys("11111111111")    # 输入新密码
        self.driver.find_element_by_xpath("//div[3]/input").send_keys("Abcd1234**")    # 确认新密码
        self.driver.find_element_by_xpath("//div/div/button").click()    # 点击确认按钮
        self.driver.find_element_by_xpath("//form/div/div/button").click()  # 选择验证方式
        self.driver.find_element_by_xpath("//div[2]/div/button").click()  # 点击获取验证码
        time.sleep(1)
        self.driver.find_element_by_xpath("//div[2]/div/input").send_keys("asdfasdf")  # 输入验证码
        self.driver.find_element_by_xpath("//div[3]/button").click()  # 点击确定
        time.sleep(1)
        self.driver.find_element_by_css_selector(".due-message-text").text    # 弹出错误提示
        self.assertTrue(text)
        print(u'弹出提示信息：%s' % text)
        
    def test05(self):
        u"""新密码错误"""
        self.driver.find_element_by_xpath("//input").send_keys("Abcd1234**")    # 输入旧密码
        self.driver.find_element_by_xpath("//div[2]/input").send_keys("11111111111")    # 输入错误密码
        self.driver.find_element_by_xpath("//div[3]/input").send_keys("11111111111")    # 确认新密码
        self.driver.find_element_by_xpath("//div/div/button").click()    # 点击确认按钮
        text = self.driver.find_element_by_css_selector(".form-group:nth-child(2) > .invalid-feedback").text    # 新密码文本框下错误提示
        self.assertTrue(text)
        print(u'弹出提示信息：%s' % text)
        
    def test06(self):
        u"""确认新密码错误"""
        self.driver.find_element_by_xpath("//input").send_keys("Abcd1234**")    # 输入旧密码
        self.driver.find_element_by_xpath("//div[2]/input").send_keys("Abcd1234**")    # 输入新密码
        self.driver.find_element_by_xpath("//div[3]/input").send_keys("11111111111")    # 确认新密码
        self.driver.find_element_by_xpath("//div/div/button").click()    # 点击确认按钮
        text = self.driver.find_element_by_css_selector(".form-group:nth-child(2) > .invalid-feedback").text    # 确认新密码文本框下错误提示
        self.assertTrue(text)
        print(u'弹出提示信息：%s' % text)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
