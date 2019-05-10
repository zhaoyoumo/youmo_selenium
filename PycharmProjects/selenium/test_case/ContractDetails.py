#-*-coding:utf-8-*- 
__author__ = 'Youmo' 

class ContractDetails(unittest.TestCase):
	u"""合约详情"""

	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.maximize_window()
		self.driver.get("https://test.xjonathan.me/sign-in")	# 登录
		self.driver.find_element_by_xpath("//input[@id='account']").send_keys("zhaoyoumo@outlook.com")
		self.driver.find_element_by_xpath("//input[@id='password']").send_keys("Abcd1234**")
		self.driver.find_element_by_xpath("//div/div/button").click()
		time.sleep(1)
		self.driver.get("https://test.xjonathan.me/trade")  # 进入交易页面
		self.driver.implicitly_wait(30)
		time.sleep(1)
		
		

