from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

s = Service('usr/local/bin/chromedriver')
driver = webdriver.Chrome(service=s)
a = ActionChains(driver)

# Storylane testing
driver.get('https://www.storylane.io/')
actions = ActionChains(driver)
wait = WebDriverWait(driver, 20)
driver.maximize_window()

#test Storyland logo as home button
logo_home = driver.find_element(By.CSS_SELECTOR, 'a[href="/"]')
logo_home.click()

#test nav bar
nav_products = driver.find_element(By.CSS_SELECTOR, 'a[href="/product"]')
nav_products.click()
time.sleep(1)
driver.back()

drop=Select(driver.find_element(By.CSS_SELECTOR, 'hover[data-w-id="00fcfdc7-ebb1-fb40-5745-c6a06eca5e8b"]'))
drop.select_by_visible_text('Solutions')
time.sleep(2)
nav_marketing = driver.find_element(By.CSS_SELECTOR, 'a[href="/marketing"]')
time.sleep(2)


time.sleep(6)