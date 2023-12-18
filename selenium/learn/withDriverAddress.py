from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

import time

# 创建Chrome浏览器选项
chrome_options = Options()

# 添加选项 去除"Chrome正在受测试软件的控制"通知
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
# 创建 WebDriver 对象，指明使用chrome浏览器驱动
driver = webdriver.Chrome(options=chrome_options,
                          service=Service(r"D:\software\webdriver\chromedriver-win64\chromedriver.exe"))



# 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
driver.get('https://www.baidu.com')

time.sleep(2)
driver.quit()
