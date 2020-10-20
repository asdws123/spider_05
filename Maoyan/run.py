from scrapy import cmdline

import os
# 获取当前路径
dirpath=os.path.dirname(os.path.abspath(__file__))
 # 切换到当前目录
os.chdir(dirpath)   

cmdline.execute('scrapy crawl maoyan -o maoyan.json'.split())