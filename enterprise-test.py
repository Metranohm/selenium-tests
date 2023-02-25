from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

s = Service('usr/local/bin/chromedriver')
driver = webdriver.Chrome(service=s)
# Random.org testing
driver.get("https://www.enterprise.com/en/home.html")

location_input = driver.find_element(By.CSS_SELECTOR, 'input[id="pickupLocationTextBox"]')
location_input.send_keys("Austin, TX")
time.sleep(3)
anchor_element = driver.find_element(By.CSS_SELECTOR, 'button[class="location-group__item-select"]')
anchor_element.click()
time.sleep(3)