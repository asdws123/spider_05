'''selenium操作鼠标 
可以用于操作下拉框'''

from selenium import webdriver
from selenium.webdriver import ActionChains
import time

#1.打开浏览器
driver=webdriver.Chrome()
driver.get('http://www.baidu.com')
#2.找到 设置 节点
set_note=driver.find_element_by_xpath('//*[@id="s-usersetting-top"]')
#3.鼠标到设置节点
ActionChains(driver).move_to_element(set_note).perform()
time.sleep(1)
#4.找到设置下高级搜索并点击
driver.find_element_by_link_text('高级搜索').click()