from selenium import webdriver
from selenium.webdriver.common.by import By 

import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

browser.find_element(By.CSS_SELECTOR,'button.btn').click()

parent_window = browser.window_handles[0]
second_window = browser.window_handles[1]
browser.switch_to.window(second_window)
"""
for x in range(5):
	browser.switch_to.window(second_window)
	time.sleep(0.3)
	browser.switch_to.window(parent_window)
	time.sleep(0.3)

"""
x_value = browser.find_element(By.CSS_SELECTOR,'span[id="input_value"]').text
expression = math.log(abs(12*math.sin(int(x_value))))

input_x = browser.find_element(By.TAG_NAME,'input')
input_x.send_keys(str(expression))

browser.find_element(By.CSS_SELECTOR,'button.btn').click()
