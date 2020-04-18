from time import sleep
class Logout():
    def logout(self,browser):
        browser.switch_to.default_content()
        browser.switch_to.frame('topFrame')
        browser.find_element_by_link_text('退出系统').click()
        alert = browser.switch_to.alert
        sleep(3)
        alert.accept()
        sleep(3)
        browser.quit()