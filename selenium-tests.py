from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

PATH = "/usr/bin/chromedriver"
s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)

driver.get("https://techwithtim.net")

link = driver.find_element((By.LINK_TEXT, "Python Programming"))
link.click()

try: 
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials"))
    )
    element.click()
except:
    driver.quit()
# print(driver.title)

# search = driver.find_element("name", "s")
# search.send_keys("test")
# search.send_keys(Keys.RETURN)

# try: 
#     main = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "main"))
#     )
    
#     articles = main.find_elements(By.TAG_NAME, "article")
#     for article in articles:
#         header = article.find_element(By.CLASS_NAME, "entry-summary")
#         print(header.text)
    
# finally:
#     driver.quit()
