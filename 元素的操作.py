from selenium import webdriver
browser=webdriver.Ie()
browser.get('https://www.baidu.com/')
#链接的文本
text = browser.find_element_by_link_text('新闻').text
browser.get('http://localhost:7003/')
username = browser.find_element_by_css_selector('#username')
password = browser.find_element_by_css_selector('#password')
button = browser.find_element_by_tag_name('button')
#元素的大小
size = username.size
#元素的位置
location = password.location
#元素的属性值
attribute=username.get_attribute('class')
#元素的标签名
tag=password.tag_name
#当期页面的标题
title=browser.title
#当前页面的地址
url=browser.current_url
#元素是否可用
shiyong=button.is_enabled()
#元素是否隐藏
xainshi=button.is_displayed()
#元素是否被选中
xuanzhong=button.is_selected()

print('文本为：',text)
print('大小为：',size)
print('元素的位置为：',location)
print('账号的class属性值为',attribute)
print('密码的标签为',tag)
print('页面的标题为',title)
print('当前页面的地址为',url)
print('密码是否可使用',shiyong)
print('密码是否显示',xainshi)
print('密码是否被选中',xuanzhong)

browser.quit()