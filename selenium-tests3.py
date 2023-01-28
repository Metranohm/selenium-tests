from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
#browser exposes an executable file
#Through Selenium test we will invoke the executable file which will then #invoke actual browser
driver = webdriver.Chrome(executable_path="usr/local/bin/chromedriver")

# navigate to Google
driver.get("https://www.google.com")
assert "Andrew" in driver.title

# find search box and enter search term
driver.find_element((By.TAG_NAME, "Projects")).click()


# find search box and enter search term
search_box = driver.find_element(By.NAME, "q")
search_box.clear()
search_box.send_keys("todd blake")
search_box.submit()

# assert that the first result has the search term in the title
assert "todd blake" in driver.title

# find search box and enter search term
search_box = driver.find_element(By.NAME, "q")
search_box.clear()
search_box.send_keys("fred schmed")
search_box.submit()

# assert that the first result has the search term in the title
assert "fred schmed" in driver.title

# close the current window
driver.close()

#open new browser window
driver = webdriver.Chrome()

# navigate to Google
driver.get("https://www.google.com")

# find search box and enter search term
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("turtles")
search_box.submit()

# assert that the first result has the search term in the title
assert "turtles" in driver.title

driver.implicitly_wait(100)

driver.get("https://www.google.com")

# find search box and enter search term
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("hairy nipples")
search_box.submit()

assert "hairy nipples" in driver.title

driver.implicitly_wait(100)

driver.get("https://www.google.com")
# find search box and enter search term
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("tom selleck")
search_box.submit()

assert "tom selleck" in driver.title

time.sleep(100)