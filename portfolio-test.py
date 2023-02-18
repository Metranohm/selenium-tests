from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
import time

s = Service('usr/local/bin/chromedriver')
driver = webdriver.Chrome(service=s)
driver.get('https://andrew-winkler-portfolio.netlify.app/')

# Find all the elements in the DOM
elements = driver.find_elements(By.CSS_SELECTOR('*'))

# Check that each element is present on the page and visible
for element in elements:
    try:
        assert element.is_displayed()
    except AssertionError:
        print(f"Element not visible: {element.tag_name} {element.get_attribute('class')}")

# Close the browser
driver.quit()