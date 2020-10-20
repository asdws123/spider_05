'''抓取网易云音乐排行榜100
url=https://music.163.com/#/discover/toplist'''
from selenium import webdriver

#无界面模式
options=webdriver.ChromeOptions()
options.add_argument('--headless')
#1.打开浏览器，输入地址
driver=webdriver.Chrome(options=options)
driver.get('https://music.163.com/#/discover/toplist')
#2..切换frame--id属性值
driver.switch_to_frame('g_iframe')
#3.获取数据
tr_list = driver.find_elements_by_xpath('//table/tbody/tr')
for tr in tr_list:
    item = {}
    item['rank'] = tr.find_element_by_xpath('.//span[@class="num"]').text
    item['name'] = tr.find_element_by_xpath('.//span[@class="txt"]/a/b').get_attribute('title').replace('\xa0', ' ')
    item['time'] = tr.find_element_by_xpath('.//span[@class="u-dur "]').text
    item['star'] = tr.find_element_by_xpath('.//div[@class="text"]').get_attribute('title')
    print(item)
#4.关闭浏览器
driver.quit()