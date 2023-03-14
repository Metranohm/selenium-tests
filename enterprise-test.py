from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

s = Service('users/documents/webdrivers/chromedriver')
driver = webdriver.Chrome(service=s)

# PHP Travels testing
driver.get('https://phptravels.com/demo/')
driver.maximize_window()

time.sleep(1)

pricing_button = driver.find_element(By.CSS_SELECTOR, 'a[class="jfHeader-menuListLink jfHeader-dynamicLink js-tracking js-myforms"')
pricing_button.click()
time.sleep(1)

driver.back()
time.sleep(1)

features_dropdown = driver.find_element(By.CSS_SELECTOR, 'a[class="jfHeader-menuListLink jfHeader-dynamicLink js-tracking"]')
features_dropdown.click()

time.sleep(1)

integrations_dropdown = driver.find_element(By.CSS_SELECTOR, 'a[class="jfHeader-menuListLink jfHeader-dynamicLink js-tracking js-integrations"]')
integrations_dropdown.click()

time.sleep(1)

company_dropdown = driver.find_element(By.CSS_SELECTOR, 'a[data-text-name="support"]')
company_dropdown.click()

time.sleep(1)

# test inputs
first_name1 = driver.find_element(By.CSS_SELECTOR, 'input[class="first_name input mb1"]')
first_name1.send_keys("Halcyon")

last_name1 = driver.find_element(By.CSS_SELECTOR, 'input[name="last_name"]')
last_name1.send_keys("&on&on")

business_name = driver.find_element(By.CSS_SELECTOR, 'input[name="business_name"]')
business_name.send_keys("Orbital Enterprises")

email_address = driver.find_element(By.CSS_SELECTOR, 'input[name="email"]')
email_address.send_keys('turdman@fire.com')

time.sleep(7)

submit2_button = driver.find_element(By.CSS_SELECTOR, 'button[id="demo"]')
submit2_button.click()

time.sleep(1)

# test signup: https://phptravels.org/register.php
driver.get('https://phptravels.org/register.php')
driver.maximize_window()

drop=Select(driver.find_element(By.CSS_SELECTOR, 'select[id="inputCountry"]'))
drop.select_by_visible_text('United States')

time.sleep(1)

input_city = driver.find_element(By.CSS_SELECTOR, 'input[id="inputCity"]')
input_city.send_keys("Austin")

time.sleep(1)

first_name2 = driver.find_element(By.CSS_SELECTOR, 'input[name="firstname"]')
first_name2.send_keys("Halcyon")

last_name2 = driver.find_element(By.CSS_SELECTOR, 'input[name="lastname"]')
last_name2.send_keys("&on&on")

register_email = driver.find_element(By.CSS_SELECTOR, 'input[id="inputEmail"]')
register_email.send_keys('turdman@fire.com')

input_phone = driver.find_element(By.CSS_SELECTOR, 'input[id="inputPhone"]')
input_phone.send_keys('512-555-5555')

company_name = driver.find_element(By.CSS_SELECTOR, 'input[id="inputCompanyName"]')
company_name.send_keys("Orbital Enterprises")

street_address1 = driver.find_element(By.CSS_SELECTOR, 'input[id="inputAddress1"]')
street_address1.send_keys("1234 Chime St.")
time.sleep(1)

input_postcode = driver.find_element(By.CSS_SELECTOR, 'input[id="inputPostcode"]')
input_postcode.send_keys('78758')

state_select = Select(driver.find_element(By.CSS_SELECTOR, 'select[id="stateselect"]'))
state_select.select_by_visible_text('Texas')

time.sleep(1)

input_moblie = driver.find_element(By.CSS_SELECTOR, 'input[name="customfield[2]"]')
input_moblie.send_keys('1234567890')

input_password1 = driver.find_element(By.CSS_SELECTOR, 'input[name="password"]')
input_password1.send_keys('password84$')

input_password2 = driver.find_element(By.CSS_SELECTOR, 'input[name="password2"]')
input_password2.send_keys('password84$')

time.sleep(1)

register_button = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
register_button.click()

time.sleep(2)


login_button = driver.find_element(By.CSS_SELECTOR, 'a[href="/login.php"]')
login_button.click()

time.sleep(2)

login_email = driver.find_element(By.CSS_SELECTOR, 'input[id="inputEmail"]')
login_email.send_keys('turdman@fire.com')

login_pw = driver.find_element(By.CSS_SELECTOR, 'input[id="inputPassword"]')
login_pw.send_keys('password84$')

time.sleep(15)

login_button2 = driver.find_element(By.CSS_SELECTOR, 'button[id="login"]')
login_button2.click()

time.sleep(6)

driver.quit()

