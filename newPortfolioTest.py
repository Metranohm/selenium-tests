
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_portfolio():
    # Setup
    s = Service('/home/metranohm/seleniumdrivers/chromedriver')
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()

    # Navigate to the portfolio
    driver.get("https://andrew-winkler-portfolio.netlify.app/")

    # Navigate to the About page
    about = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "About")))
    about.click()
    time.sleep(2)  # Let the user see the page
    driver.back()

    # Navigate to the Contact page
    contact = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Contact")))
    contact.click()
    time.sleep(2)  # Let the user see the page
    driver.back()

    # Navigate to the Projects page and visit each project
    projects = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Projects")))
    projects.click()

    project_links = driver.find_elements(By.CLASS_NAME, 'project-link')  # adjust this if necessary

    for link in project_links:
        time.sleep(2)  # Let the user see the page
        link.click()
        time.sleep(2)  # Let the user see the page
        driver.back()

    driver.back()

    # Navigate to the Resume page and download the resume
    resume = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Resume")))
    resume.click()

    # Assuming resume is available to download as a button or link
  

    time.sleep(2)  # Let the download finish

    # Clean up
    driver.quit()

if __name__ == "__main__":
    test_portfolio()
# Please replace the placeholders (By.CLASS_NAME, 'project-link' and By.ID, 'download-button') with actual values according to your website's DOM structure. This script is only a starting point and might need to be adjusted to fit your specific website structure and needs.

# Also, downloading files using Selenium might need additional browser preferences to be set, depending on the browser configuration and whether it's allowed to automatically download files.




