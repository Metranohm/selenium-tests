from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time

s=Service('/snap/bin/geckodriver')
driver = webdriver.Firefox(service=s)


driver.maximize_window()
driver.get('https://rahulshettyacademy.com')
print(driver.title)
print(driver.current_url)

driver.close()