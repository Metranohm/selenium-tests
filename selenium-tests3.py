from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--headless")

# set up webdriver
driver = webdriver.Chrome(chrome_options=options)

# navigate to Google
driver.get("https://www.google.com")

# find search box and enter search term
search_box = driver.find_element_by_name("q")
search_box.send_keys("andrew winkler")
search_box.submit()

# assert that the first result has the search term in the title
assert "andrew winkler" in driver.title

# close browser
driver.quit()
