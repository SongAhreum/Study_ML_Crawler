from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

url ="https://www.naver.com/"
browser = webdriver.Chrome()
browser.get(url)
time.sleep(1) #10초동안 browser 켜져있음

login = browser.find_element(By.CLASS_NAME,'MyView-module__link_login___HpHMW')
login.click()
time.sleep(2)

id = browser.find_element(By.ID,'id')
id.send_keys('thddkfmathd')
pw = browser.find_element(By.ID,'pw')
pw.send_keys('thddkfma2260!')
time.sleep(1)

btn_login = browser.find_element(By.ID,'log.login')
btn_login.click()
time.sleep(2)