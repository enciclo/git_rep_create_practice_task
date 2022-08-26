from selenium import webdriver
from selenium.webdriver.common.by import By 

import time
import math
link = "http://SunInJuly.github.io/execute_script.html"

browser = webdriver.Chrome()
browser.get(link)

#Тест скрывания footer при помощи JS 
footer = browser.find_element(By.TAG_NAME,'footer')
browser.execute_script('arguments[0].style.visibility = \'hidden\'', footer)


x_value = browser.find_element(By.CSS_SELECTOR,'span[id="input_value"]').text
expression = math.log(abs(12*math.sin(int(x_value))))

input_x = browser.find_element(By.TAG_NAME,'input')
input_x.send_keys(str(expression))

i_am_robot = browser.find_element(By.CSS_SELECTOR,'[for="robotCheckbox"]')
browser.execute_script("return arguments[0].scrollIntoView(true);", i_am_robot)
i_am_robot.click()

robots_rule = browser.find_element(By.CSS_SELECTOR,'[for="robotsRule"]')
browser.execute_script("return arguments[0].scrollIntoView(true);", robots_rule)
robots_rule.click()

button = browser.find_element(By.TAG_NAME,"button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

