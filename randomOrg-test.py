from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os

s = Service('usr/local/bin/chromedriver')
driver = webdriver.Chrome(service=s)
driver.get("https://www.random.org/integers")

num_numbers = driver.find_element(By.CSS_SELECTOR, 'input[name="num"]')
num_numbers.clear()
num_numbers.send_keys("10")
submit_button = driver.find_element(By.CSS_SELECTOR, 'input[value="Get Numbers"]')
submit_button.click()
time.sleep(10)