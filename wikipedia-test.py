from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the browser and navigate to the Wikipedia homepage
browser = webdriver.Chrome()
browser.get("https://en.wikipedia.org/wiki/Main_Page")

# Get all the links in the navigation bar
nav_links = browser.find_elements(By.CSS_SELECTOR, "#mp-topbanner a")

# Loop through each link and test if it is clickable
for link in nav_links:
    try:
        # Wait for the link to become clickable
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, f"a[href='{link.get_attribute('href')}']")))
        # Click the link
        link.click()
        # Wait for the new page to load
        WebDriverWait(browser, 5).until(EC.title_contains("Wikipedia"))
        # Navigate back to the homepage
        browser.back()
    except Exception as e:
        print(f"Failed to click on link: {link.get_attribute('href')}. Exception: {e}")

# Close the browser
browser.quit()
