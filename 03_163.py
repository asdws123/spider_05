"""
selenium模拟登录163邮箱
思路：
    1、切换iframe - 此处iframe节点中id的值每次都在变化,需要手写xpath,否则会出现无法定位iframe
    2、输入用户名和密码
    3、点击登录按钮
"""
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://mail.163.com/')

# 1、切换iframe子页面 - 此处手写xpath,此处iframe中id的值每次都在变化
node = driver.find_element_by_xpath('//div[@id="loginDiv"]/iframe[1]')
driver.switch_to.frame(node)

# 2、输入用户名和密码
driver.find_element_by_name('email').send_keys('wangweichao_2020')
driver.find_element_by_name('password').send_keys('zhanshen001')
driver.find_element_by_id('dologin').click()