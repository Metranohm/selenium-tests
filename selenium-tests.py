from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "/usr/bin/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://techwithtim.net")
print(driver.title)

search = driver.find_element("name", "s")
search.send_keys("test")
search.send_keys(Keys.RETURN)

main = driver.find_element("id", "main")
print(main.text)


driver.quit()