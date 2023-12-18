#lib\webui.py

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service

def loginAndCheck(username,password):
    # 创建Chrome浏览器选项
    chrome_options = Options()

    # 添加选项 去除"Chrome正在受测试软件的控制"通知
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    driver = webdriver.Chrome(options=chrome_options,service=Service(r"D:\software\webdriver\chromedriver-win64\chromedriver.exe"))
    driver.implicitly_wait(10)

    driver.get('http://127.0.0.1/mgr/sign.html')

    if username:
        driver.find_element(By.ID,'username').send_keys(username)
    if password:
        driver.find_element(By.ID,'password').send_keys(password)

    driver.find_element(By.XPATH,"//button[@class='btn btn-primary btn-block btn-flat' and text()='登录']").click()

    time.sleep(2)

    try:
        alert = WebDriverWait(driver, 2).until(EC.alert_is_present())
        returnText = alert.text
        print(returnText)
        return returnText
    except TimeoutException:
        print("Login Success!")
        return 'success'
    driver.quit()

#直接测试入口
loginAndCheck('byhy','88888888')
