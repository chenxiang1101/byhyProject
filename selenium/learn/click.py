import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.byhy.net/_files/stock1.html')
driver.implicitly_wait(3)
input = driver.find_element(By.ID,'kw').send_keys('四川')
driver.find_element(By.ID,'go').click()
time.sleep(5)

driver.quit()