from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from tkinter import *
import tkinter as tk
import time

s = Service('usr/local/bin/chromedriver')
driver = webdriver.Chrome(service=s)

# PHP Travels testing
driver.get('https://www.random-name-generator.com/united-states')
driver.maximize_window()
print(driver.title)
print(driver.current_url)

set_single = driver.find_element(By.XPATH, "//input[@type='number']")
set_single.clear()
set_single.send_keys("1")

generate_button = driver.find_element(By.XPATH, "//button[@type='submit']")
generate_button.click()

time.sleep(1)

copyname_button = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[3]/div[2]/div[1]/div[1]/ul[1]/li[1]/span[1]/button[1]/img[1]").click()
root = tk.Tk()
new_name = root.clipboard_get()
print(new_name)

time.sleep(1)

driver.get('https://andrews-js-password-generator.netlify.app/')

driver.find_element(By.ID, 'length').clear()
driver.find_element(By.ID, 'length').send_keys('10')
driver.find_element(By.ID, 'include-numbers').click()
driver.find_element(By.CSS_SELECTOR, 'button[id="generate-button"]').click()
copy_button = driver.find_element(By.ID, 'copy-button').click()
root = tk.Tk()
new_pw = root.clipboard_get()
print(new_pw)


driver.quit() 