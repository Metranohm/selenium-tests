from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
import time

s = Service('usr/local/bin/chromedriver')
driver = webdriver.Chrome(service=s)

driver.get("https://orteil.dashnet.org/cookieclicker/")

time.sleep(10)

cookie = driver.find_element(By.ID, "bigCookie")
cookie_count = driver.find_element(By.ID, "cookies")
items = [driver.find_element(By.ID, "productPrice" + str(i)) for i in range(1, -1, -1)]

actions = ActionChains(driver)
actions.click(cookie)

for i in range (5000):
    actions.perform()
    count = cookie_count.text
    print(count)
