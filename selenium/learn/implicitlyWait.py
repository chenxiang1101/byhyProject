import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get('https://www.byhy.net/_files/stock1.html')

element = driver.find_element(By.ID, 'kw')

element.send_keys('通讯\n')


# 返回页面 ID为1 的元素
element = driver.find_element(By.ID,'1')

print(element.text)
time.sleep(3)
driver.quit()