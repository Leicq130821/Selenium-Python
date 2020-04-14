from selenium import webdriver

options = webdriver.ChromeOptions()
options.binary_location=r'E:\常用软件\360浏览器\360se6\Application\360se.exe'
driver = webdriver.Chrome(r'E:\WebDriver\chromedriver_v2.36.exe', options=options)
driver.get('http://127.0.0.1/biz/user-login-L2Jpei8=.html')
driver.find_element_by_id('account').send_keys('admin')
driver.find_element_by_name('password').send_keys('000000')
driver.find_element_by_id('submit').click()