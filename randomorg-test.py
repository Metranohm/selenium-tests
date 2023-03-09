from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

s = Service('usr/local/bin/chromedriver')
driver = webdriver.Chrome(service=s)

# random.org testing
driver.get("https://www.random.org/integers")
driver.maximize_window() 
  
# test 1

num_nums = driver.find_element(By.CSS_SELECTOR, 'input[name="num"]')
num_nums.clear()

num_nums.send_keys("10")

min_nums = driver.find_element(By.CSS_SELECTOR, 'input[name="min"]')
min_nums.clear()
min_nums.send_keys("3")

max_nums = driver.find_element(By.CSS_SELECTOR, 'input[name="max"]')
max_nums.clear()

max_nums.send_keys("10000")
submit_button = driver.find_element(By.CSS_SELECTOR, 'input[value="Get Numbers"]')
submit_button.click()

rand_nums = driver.find_element(By.XPATH, '//pre[@class="data"]').text
print(rand_nums)

driver.get('https://www.google.com')
driver.find_element(By.NAME, 'q').send_keys(rand_nums)

time.sleep(30)
driver.quit()
# reset_button = driver.find_element(By.CSS_SELECTOR, 'input[value="Reset Form"]')
# reset_button.click()
# time.sleep(2)

# # test 2
# num_numbers = driver.find_element(By.CSS_SELECTOR, 'input[name="num"]')
# num_numbers.clear()
# num_numbers.send_keys("125")
# time.sleep(1)
# min_nums = driver.find_element(By.CSS_SELECTOR, 'input[name="min"]')
# min_nums.clear()
# min_nums.send_keys("60")
# time.sleep(1)
# max_nums = driver.find_element(By.CSS_SELECTOR, 'input[name="max"]')
# max_nums.clear()
# max_nums.send_keys("10000")
# column_input = driver.find_element(By.CSS_SELECTOR, 'input[name="col"]')
# column_input.clear()
# column_input.send_keys("10")
# time.sleep(1)
# submit_button = driver.find_element(By.CSS_SELECTOR, 'input[value="Get Numbers"]')
# submit_button.click()
# time.sleep(3)
# driver.back()
# time.sleep(1)
# advance_button = driver.find_element(By.CSS_SELECTOR, 'input[value="Switch to Advanced Mode"]')
# advance_button.click()
# time.sleep(10)