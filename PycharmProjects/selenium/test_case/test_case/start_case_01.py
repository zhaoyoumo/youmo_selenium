#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import sleep

import win32api
import win32con
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

__author__ = 'Youmo'

# 1.先用selenium打开你需要的登录的页面地址url1
driver = webdriver.Firefox()
driver.maximize_window()
driver.get('https://m.cokeway.info/')
print("1.进入app")
sleep(3)

driver.find_element_by_xpath("//div[4]/div[2]/div/div[3]/div[2]").click()
sleep(1)
print("-> 弹窗：点击确定")

driver.find_element_by_xpath("//p[text()='我的']").click()
print ("2.点击我的页面")
sleep(1)

driver.find_element_by_xpath("//*[contains(text(),'登录/注册')]").click()
print ("3.点击登录/注册")

driver.find_element_by_css_selector("input[type='text']").send_keys("17710151109")
driver.find_element_by_css_selector("input[type='password']").send_keys("495889504zlk")
print("4.输入用户名密码")

# 鼠标悬停在验证码上
vertifyimg = xpath_button_add_condition = ("//img")
move_on_to_add_condition = driver.find_element_by_xpath(vertifyimg)
ActionChains(driver).move_to_element(move_on_to_add_condition).perform()
sleep(2)

# 鼠标右击:
vertifyimg = driver.find_element_by_xpath("//img")


#表示键盘方向键的下，后面附键位表
action = ActionChains(driver)
action.context_click(vertifyimg).perform()
sleep(1)
win32api.keybd_event(40,win32con.KEYEVENTF_KEYUP,0).keybd_event(40,win32con.KEYEVENTF_KEYUP,0).keybd_event(40,win32con.KEYEVENTF_KEYUP,0) # 向下
win32api.keybd_event(13,win32con.KEYEVENTF_KEYUP,0)#然后enter按下
print("5.右键复制验证码链接")


# 2.通过审核元素获取验证码的地址url2（其实最简单的是右键打开新页面）
# 新开一个窗口，通过执行js来新开一个窗口
# js = 'window.open();
# driver.execute_script(js)

# 3：在url1页面，输入地址url2进入url2页面，然后截屏保存验证码页面
# 4：处理验证码得到验证码字符串。然后点击浏览器后退按钮，返回url1登录页面
# 5：输入登录需要的信息和验证码
# 6：点击登录
# 7：验证登录后的页面，判断是否成功，若不成功则需要重新1-7的操作
