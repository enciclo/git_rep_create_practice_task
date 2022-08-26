from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.implicitly_wait(12)
browser.get(link)
price_block = WebDriverWait(browser,12).until(
		EC.text_to_be_present_in_element((By.CSS_SELECTOR,'[id="price"]'),"$100")
	)

browser.find_element(By.CSS_SELECTOR,'button.btn').click()

x_value = browser.find_element(By.CSS_SELECTOR,'[id="input_value"]').text
expression = str(math.log(abs(12*math.sin(int(x_value)))))
input_box = browser.find_element(By.CSS_SELECTOR,'[id="answer"]')
input_box.send_keys(expression)
browser.find_element(By.CSS_SELECTOR,'[type="submit"]').click()

