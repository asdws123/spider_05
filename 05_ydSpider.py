"""
selenium抓取有道翻译结果
"""

from selenium import webdriver
import time

class YdSpider:
    def __init__(self):
        # 无界面
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get(url='http://fanyi.youdao.com/')

    def get_result(self, word):
        self.driver.find_element_by_xpath('//*[@id="inputOriginal"]').send_keys(word)
        # 给页面元素加载预留时间
        time.sleep(1)
        result = self.driver.find_element_by_xpath('//*[@id="transTarget"]/p/span').text

        return result

    def run(self):
        word = input('请输入要翻译的单词:')
        result = self.get_result(word)
        print(result)

if __name__ == '__main__':
    spider = YdSpider()
    spider.run()


