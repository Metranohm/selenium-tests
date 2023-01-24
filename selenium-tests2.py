from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()

# Navigate to the portfolio website
driver.get("https://andrew-winkler-portfolio.netlify.app/")

# Find all project links on the page
project_links = driver.find_elements_by_css_selector("a.project-link")

# Iterate through each project link and open it
for link in project_links:
    link.click()
    driver.back()

# Close the browser window
driver.quit()