#Работа со списками
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

numbers = [int(num.text) for num in browser.find_elements(By.XPATH,'//span[contains(@id,"num")]')]
sum_value = sum(numbers)
print(sum_value)

select = Select(browser.find_element(By.TAG_NAME,"select"))
select.select_by_value(str(sum_value))
browser.find_element(By.CSS_SELECTOR, "button.btn").click()

time.sleep(15)
browser.quit()

