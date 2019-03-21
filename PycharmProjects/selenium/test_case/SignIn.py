#-*-coding:utf-8-*-
import time
from selenium import webdriver

__author__ = 'Youmo'


driver = webdriver.Chrome()
driver.get("https://test.xjonathan.me/sign-in")    # 打开测试地址
time.sleep(1)
driver.find_element_by_id("account").send_keys("zhaoyoumo@outlook.com")     # 点击登录
driver.find_element_by_id("password").send_keys("Abcd1234**")
driver.find_element_by_xpath("//div/div/button").click()




time.sleep(3)
driver.quit()