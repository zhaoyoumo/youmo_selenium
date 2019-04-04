# -*-coding:utf-8-*-

import time

from selenium import webdriver

__author__ = 'Youmo'

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://test.xjonathan.me/sign-in")
driver.find_element_by_id("account").send_keys("zhaoyoumo@outlook.com")
driver.find_element_by_id("password").send_keys("Abcd1234**")
driver.find_element_by_xpath("//div/div/button").click()
time.sleep(1)
driver.get("https://test.xjonathan.me/trade")
time.sleep(1)
driver.find_element_by_css_selector(".form-control:nth-child(1)").send_keys(10)
driver.find_element_by_xpath("//div[3]/div[2]/div").click()
time.sleep(1)
driver.find_element_by_xpath("//div[2]/input").send_keys("4000")
driver.find_element_by_xpath("//div[3]/input").send_keys("1000")
driver.find_element_by_xpath("//button/span[2]").click()
time.sleep(1)
#  获取提示信息
message = driver.find_element_by_xpath("//span/div/div/div/div/div").text()
# 断言实际结果与期望结果一致
# self.assertTrue(error_message)
print (u"弹出提示：%s" % message)
time.sleep(3)

driver.quit()
