from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


s=Service('/usr/bin/chromedriver')

driver = webdriver.Chrome(service=s)
driver.get("https://rahulshettyacademy.com/client")

driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com")
driver.find_element(By.CSS_SELECTOR, "#userPassword").send_keys("hello@1234")
driver.find_element(By.XPATH, "//form/div[3]/input").send_keys("hello@1234")
driver.find_element(By.XPATH, "//button[text()='Save New Password']").click()

time.sleep(20)