from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import tkinter as tk
import time

s=Service('/snap/bin/chromedriver')
driver = webdriver.Chrome(service=s)
driver.maximize_window()

#
driver.get('https://andrews-js-password-generator.netlify.app/')
print(driver.title)
print(driver.current_url)

driver.find_element(By.ID, 'length').clear()
driver.find_element(By.ID, 'length').send_keys('10')
driver.find_element(By.ID, 'include-numbers').click()
driver.find_element(By.CSS_SELECTOR, 'button[id="generate-button"]').click()
time.sleep(1)
copy_button = driver.find_element(By.ID, 'copy-button').click()
root = tk.Tk()
new_pw = root.clipboard_get()




driver.close()