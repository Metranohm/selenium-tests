from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

s = Service('usr/local/bin/chromedriver')
driver = webdriver.Chrome(service=s)
# Random.org testing
driver.get("https://www.random.org/integers")

num_numbers = driver.find_element(By.CSS_SELECTOR, 'input[name="num"]')
num_numbers.clear()
num_numbers.send_keys("10")
submit_button = driver.find_element(By.CSS_SELECTOR, 'input[value="Get Numbers"]')
submit_button.click()
time.sleep(3)
driver.back()
time.sleep(3)
num_numbers = driver.find_element(By.CSS_SELECTOR, 'input[name="num"]')
num_numbers.clear()
num_numbers.send_keys("1000")
time.sleep(3)
submit_button = driver.find_element(By.CSS_SELECTOR, 'input[value="Get Numbers"]')
submit_button.click()
time.sleep(3)
driver.back()
# PHP Travels testing
driver.get('https://phptravels.com/demo/')
time.sleep(1)
first_name = driver.find_element(By.CSS_SELECTOR, 'input[class="first_name input mb1"]')
first_name.send_keys("Andrew")
last_name = driver.find_element(By.CSS_SELECTOR, 'input[name="last_name"]')
last_name.send_keys("Winkler")
business_name = driver.find_element(By.CSS_SELECTOR, 'input[name="business_name"]')
business_name.send_keys("Winkler Enterprises")
email_address = driver.find_element(By.CSS_SELECTOR, 'input[name="email"]')
email_address.send_keys('andrewwink@gmail.com')
time.sleep(10)
submit2_button = driver.find_element(By.CSS_SELECTOR, 'button[id="demo"]')
submit2_button.click()
time.sleep(7)
driver.quit()

