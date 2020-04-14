from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
driver=webdriver.Ie()
driver.maximize_window()
#隐式等待
# driver.implicitly_wait(20)
driver.get('http://localhost:9085')
#显示等待
element=(By.ID,"username1")
wait=WebDriverWait(driver,10,poll_frequency=0.5)
wait.until(EC.presence_of_element_located(element)).send_keys('admin')
driver.find_element('id','password').send_keys('000000')
driver.find_element(By.CLASS_NAME,'loginbtn').click()

sleep(3)
driver.quit()