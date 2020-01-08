from time import sleep
from selenium import webdriver
browser = webdriver.Ie()
browser.get('http://localhost:7003')
browser.find_element_by_xpath("//input[@tabIndex='1'and @id='username']").send_keys('admin')
browser.find_element_by_xpath("//input[starts-with(@name,'password')]").send_keys('000000')
browser.find_element_by_xpath("//button[contains(@class,'cssLoginBtn_L1')]").click()
sleep(5)
browser.get('http://www.baidu.com')
browser.find_element_by_xpath("//a[text()='新闻']").click()
sleep(5)
browser.quit()