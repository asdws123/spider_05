"""
selenium执行js脚本
"""

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get(url='https://www.jd.com/')

# 搜索框发送关键字  点击搜索按钮
driver.find_element_by_xpath('//*[@id="key"]').send_keys('爬虫书')
driver.find_element_by_xpath('//*[@id="search"]/div/div[2]/button').click()
time.sleep(1)

# 进入到了商品页面
# 将进度条拉到底部
driver.execute_script(
    'window.scrollTo(0,document.body.scrollHeight)'
)
# 给页面元素加载预留时间
time.sleep(2)

# 提取具体数据
li_list = driver.find_elements_by_xpath('//*[@id="J_goodsList"]/ul/li')
for li in li_list:
    print(li.text)
    print('*' * 50)












