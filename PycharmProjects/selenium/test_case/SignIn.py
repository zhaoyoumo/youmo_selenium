# -*-coding:utf-8-*-
import time
from selenium import webdriver

__author__ = 'Youmo'

driver = webdriver.Chrome()
driver.get("https://test.xjonathan.me/sign-in")
time.sleep(1)
account = driver.find_element_by_id("account").send_keys("zhaoyoumo@outlook.com")
psw = driver.find_element_by_id("password").send_keys("Abcd1234**")
driver.find_element_by_xpath("//div/div/button").click()

time.sleep(1)
driver.quit()

driver = webdriver.Chrome()
driver.get("https://test.xjonathan.me/sign-in")
time.sleep(1)

if account == driver.find_element_by_id("account").click():
    driver.find_element_by_xpath("//div/div/button").click()
    feedback_1 = driver.find_element_by_xpath("//form/div/div").text
    print (u"获取到的提示：%s" % feedback_1)

    if feedback_1 == u"请输入邮箱/手机号":
        print u"登录失败"
    else:
        print u"登录成功"
        time.sleep(1)

if account == driver.find_element_by_id("account").send_keys("10000000000"):
    print u"输入错误的账户"
    driver.find_element_by_xpath("//div/div/button").click()
    feedback_2 = driver.find_element_by_xpath("//form/div/div").text
    print (u"获取到的提示：%s" % feedback_2)
    if feedback_2 == u"!!passwordNull!!":
        print u"密码输入为空，登录失败"
    else:
        print u"登录成功"
        time.sleep(1)

driver.quit()
