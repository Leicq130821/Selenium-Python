from selenium import webdriver

# 指定浏览器的运行内核。
options = webdriver.ChromeOptions()
# 指定启动程序。
options.binary_location=r'E:\常用软件\360浏览器\360se6\Application\360se.exe'
# 实例化浏览器指定驱动。
driver = webdriver.Chrome(r'E:\WebDriver\chromedriver_v2.36.exe', options=options)