class Browser():
    def WEB(browser):
        from selenium import webdriver
        if browser['browser']=='IE':
            driver=webdriver.Ie()
        elif browser['browser']=='FIRE':
            driver = webdriver.Firefox()
        elif browser['browser']=='CHROME':
            driver = webdriver.Chrome()
        driver.maximize_window()
        return driver
    def URL(driver,url):
        driver.get(url['url'])