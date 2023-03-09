from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

s = Service('usr/local/bin/chromedriver')
driver = webdriver.Chrome(service=s)

# PHP Travels testing
driver.get('https://www.random-name-generator.com/united-states')
driver.maximize_window()

set_single = driver.find_element(By.XPATH, "//input[@type='number']")
set_single.clear()
set_single.send_keys("1")

generate_button = driver.find_element(By.XPATH, "//button[@type='submit']")
generate_button.click()

time.sleep(1)
copied_name = driver.find_element(By.XPATH, "//button[@class='btn-copy-name']").text
print(copied_name)




time.sleep(300)