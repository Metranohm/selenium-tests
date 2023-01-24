from selenium import webdriver

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()

# Navigate to the website
driver.get("https://andrew-winkler-portfolio.netlify.app/")

# Get all the links on the page
links = driver.find_elements(By.TAG_NAME, "a")

# Visit each link
for link in links:
    href = link.get_attribute("href")
    driver.get(href)

# Close the browser
driver.quit()