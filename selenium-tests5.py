from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
#browser exposes an executable file
#Through Selenium test we will invoke the executable file which will then #invoke actual browser
driver = webdriver.Chrome(executable_path="usr/local/bin/chromedriver")

# navigate to Google
driver.get("https://andrew-winkler-portfolio.netlify.app/")
time.sleep(5)

driver.find_element((By.ID, "projects-navLink")).click()
time.sleep(5)