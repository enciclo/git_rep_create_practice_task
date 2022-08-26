#Работа с загрузкой файла
from selenium import webdriver
from selenium.webdriver.common.by import By 

import time
import os

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

inputs = browser.find_elements(By.CSS_SELECTOR,'input[type="text"]')
for input in inputs:
	input.send_keys("Any Value")

with open('test_file.txt', 'w') as file:
   file.write('test_data for Course Stepik')

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'test_file.txt')           # добавляем к этому пути имя файла 


browser.find_element(By.CSS_SELECTOR,'input[type="file"]').send_keys(file_path)

browser.find_element(By.CSS_SELECTOR,'button.btn').click()
