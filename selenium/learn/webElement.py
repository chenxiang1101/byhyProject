import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://cdn2.byhy.net/files/selenium/sample1.html')

element = driver.find_element(By.ID,'container')

# 限制 选择元素的范围是 id 为 container 元素的内部。
spans = element.find_elements(By.TAG_NAME, 'span')
for span in spans:
    print(span.text)

time.sleep(3)
driver.quit()