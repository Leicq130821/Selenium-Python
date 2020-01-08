from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Ie()
browser.get('http://localhost:7003/')
#显示等待
element = (By.CSS_SELECTOR,'#username')
wait = WebDriverWait(browser,5,poll_frequency=1,ignored_exceptions='等待超时')
action = wait.until(EC.presence_of_element_located(element))
action.send_keys('admin')
#隐式等待—全局元素
browser.implicitly_wait(5)