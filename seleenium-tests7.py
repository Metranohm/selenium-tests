from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
#browser exposes an executable file
#Through Selenium test we will invoke the executable file which will then #invoke actual browser
driver = webdriver.Chrome(executable_path="usr/local/bin/chromedriver")

driver.get('https://www.yahoo.com')

search_box = driver.find_element(By.NAME, "q")
search_box.clear()
search_box.send_keys("electric slide")
search_box.submit()

