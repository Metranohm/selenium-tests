from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="usr/local/bin/chromedriver")

driver.get("https://andrew-winkler-portfolio.netlify.app/")

link = driver.find_element((By.LINK_TEXT, "Projects"))

driver.implicitly_wait(5)

link = driver.find_element((By.CLASS_NAME, "ProjectPreview_img__9yc2u"))

driver.implicitly_wait(5)

link = driver.find_element((By.LINK_TEXT, "View deployed"))

