from time import sleep

class Login():
    def login(self,browser,username,password):
        browser.find_element_by_id('username').send_keys(username)
        browser.find_element_by_id('password').send_keys(password)
        browser.find_element_by_tag_name('button').click()
        sleep(3)