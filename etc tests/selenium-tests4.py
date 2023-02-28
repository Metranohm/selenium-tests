from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
#browser exposes an executable file
#Through Selenium test we will invoke the executable file which will then #invoke actual browser
driver = webdriver.Chrome(executable_path="usr/local/bin/chromedriver")

driver.get('https://andrew-winkler-portfolio.netlify.app/')
time.sleep(5)
link = driver.find_element((By.LINK_TEXT, "projects"))
link.click()

time.sleep(5)


link = driver.find_element((By.CLASS_NAME, "ProjectPreview_h3__dE+pg"))
link.click()
time.sleep(5)

link = driver.find_element((By.LINK_TEXT, "View deployed"))
link.click()

time.sleep(50)

