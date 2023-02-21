from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
import time

s = Service('usr/local/bin/chromedriver')
driver = webdriver.Chrome(service=s)
driver.get('https://andrew-winkler-portfolio.netlify.app/')

about = driver.find_element(By.LINK_TEXT, "About")

about.click()

time.sleep(100)