from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time
#browser exposes an executable file
#Through Selenium test we will invoke the executable file which will then #invoke actual browser
driver = webdriver.Chrome(executable_path="usr/local/bin/chromedriver")

driver.get("https://google.com")

# Locate the search bar and input the search query
search_bar = driver.find_element_by_name("q")
search_bar.send_keys("black-footed ferrets")
search_bar.send_keys(Keys.RETURN)

# Wait for the search results to load
wait = WebDriverWait(driver, 10)
results = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.r a")))

# Select the 3rd search result
result = results[2]
result.click()
