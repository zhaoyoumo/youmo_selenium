#-*-coding:utf-8-*-
import time

__author__ = 'Youmo'

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://192.168.1.214/")
print (driver.title)
time.sleep(3)

driver.find_element_by_xpath("//*[contains(text(),'动态')]").click()
time.sleep(2)
print("点击【动态】")

driver.find_element_by_xpath("//*[contains(text(),'帮助')]").click()
time.sleep(2)
print("点击帮助】")
