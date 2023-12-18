import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()

driver.get('https://www.baidu.com')
try:
    input = driver.find_element(By.ID,'kw1').send_keys('python')
except NoSuchElementException:
    pass
time.sleep(3)

driver.quit()