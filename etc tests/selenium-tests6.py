from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
#browser exposes an executable file
#Through Selenium test we will invoke the executable file which will then #invoke actual browser
driver = webdriver.Chrome(executable_path="usr/local/bin/chromedriver")

# navigate to Google
driver.get("https://www.google.com")

# find search box and enter search term
search_box = driver.find_element(By.NAME, "q")
search_box.clear()
search_box.send_keys("python")
search_box.submit()

# assert that the first result has the search term in the title

search_box = driver.find_element(By.NAME, "q")
search_box.clear()
search_box.send_keys("java")
search_box.submit()

time.sleep(50)

