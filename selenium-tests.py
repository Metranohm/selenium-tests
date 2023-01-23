from selenium import webdriver

PATH = "home/metranohm/code/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://techwithtim.net")
print(driver.title)
driver.quit()