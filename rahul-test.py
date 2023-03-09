from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time

s=Service('/snap/bin/chromedriver')
driver = webdriver.Chrome(service=s)


driver.maximize_window()
driver.get('https://andrews-js-password-generator.netlify.app/')
print(driver.title)
print(driver.current_url)

driver.find_element(By.ID, 'length').clear()
driver.find_element(By.ID, 'length').send_keys('10')
driver.find_element(By.ID, 'include-numbers').click()
driver.find_element(By.CSS_SELECTOR, 'button[id="generate-button"]').click()
time.sleep(1)
new_pw = driver.find_element(By.CSS_SELECTOR, 'input[id="password"]').text
print(new_pw)

driver.close()