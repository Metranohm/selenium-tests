from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time

s = Service('usr/local/bin/chromedriver')
driver = webdriver.Chrome(service=s)
browser = webdriver.Chrome()

# navigate to the website
driver.get("https://andrew-winkler-portfolio.netlify.app/")

# get all the links in the navigation bar
nav_links = browser.find_elements(By.CSS_SELECTOR, "NavBar_name__ZPtL0")

# iterate over each link and click it
for link in nav_links:
    link.click()
    
    # wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
    
    # go back to the home page
    driver.back()

# close the browser
driver.quit()