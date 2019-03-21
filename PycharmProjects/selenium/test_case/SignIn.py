#-*-coding:utf-8-*-
import time
from selenium import webdriver

__author__ = 'Youmo'


driver = webdriver.Chrome()
driver.get("https://test.xjonathan.me/")    # 打开测试地址
time.sleep(1)
driver.find_element_by_xpath(u"//button[contains(.,'注册')]").click() # 点击注册按钮
driver.find_element_by_id("country").click()
driver.find_element_by_xpath("//input[@type='email']").send_keys("zhaolikun@delphy.org")
driver.find_element_by_xpath("//input[@type='password']").send_keys("495889504@Zlk")
driver.find_element_by_xpath("(//input[@type='password'])[2]").send_keys("495889504@Zlk")
driver.find_element_by_css_selector(".custom-checkbox").click()
driver.find_element_by_xpath("(//button[@type='button'])[4]").click()



time.sleep(3)
driver.quit()