from selenium import webdriver
from selenium.webdriver.common.by import By 

import time
import math

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element(By.CSS_SELECTOR,'button.btn')
button.click()

confirm = browser.switch_to.alert
confirm.accept()

x_value = browser.find_element(By.CSS_SELECTOR,'span[id="input_value"]').text
expression = math.log(abs(12*math.sin(int(x_value))))

input_x = browser.find_element(By.TAG_NAME,'input')
input_x.send_keys(str(expression))

browser.find_element(By.CSS_SELECTOR,'button.btn').click()

