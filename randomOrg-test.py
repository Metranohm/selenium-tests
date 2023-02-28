from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

s = Service('usr/local/bin/chromedriver')
driver = webdriver.Chrome(service=s)

## random.org testing
# driver.get("https://www.random.org/integers")
# driver.maximize_window() 
  
# # test 1
# time.sleep(1)
# num_nums = driver.find_element(By.CSS_SELECTOR, 'input[name="num"]')
# num_nums.clear()
# time.sleep(1)
# num_nums.send_keys("10")
# time.sleep(1)
# min_nums = driver.find_element(By.CSS_SELECTOR, 'input[name="min"]')
# min_nums.clear()
# min_nums.send_keys("3")
# time.sleep(1)
# max_nums = driver.find_element(By.CSS_SELECTOR, 'input[name="max"]')
# max_nums.clear()
# time.sleep(1)
# max_nums.send_keys("10000")
# reset_button = driver.find_element(By.CSS_SELECTOR, 'input[value="Reset Form"]')
# reset_button.click()
# time.sleep(2)

# # test 2
# num_numbers = driver.find_element(By.CSS_SELECTOR, 'input[name="num"]')
# num_numbers.clear()
# num_numbers.send_keys("125")
# time.sleep(1)
# min_nums = driver.find_element(By.CSS_SELECTOR, 'input[name="min"]')
# min_nums.clear()
# min_nums.send_keys("60")
# time.sleep(1)
# max_nums = driver.find_element(By.CSS_SELECTOR, 'input[name="max"]')
# max_nums.clear()
# max_nums.send_keys("10000")
# column_input = driver.find_element(By.CSS_SELECTOR, 'input[name="col"]')
# column_input.clear()
# column_input.send_keys("10")
# time.sleep(1)
# submit_button = driver.find_element(By.CSS_SELECTOR, 'input[value="Get Numbers"]')
# submit_button.click()
# time.sleep(3)
# driver.back()
# time.sleep(1)
# advance_button = driver.find_element(By.CSS_SELECTOR, 'input[value="Switch to Advanced Mode"]')
# advance_button.click()
# time.sleep(3)

# # PHP Travels testing
# driver.get('https://phptravels.com/demo/')
# driver.maximize_window()
# time.sleep(1)
# pricing_button = driver.find_element(By.CSS_SELECTOR, 'a[class="jfHeader-menuListLink jfHeader-dynamicLink js-tracking js-myforms"')
# pricing_button.click()
# time.sleep(1)
# driver.back()
# time.sleep(1)
# features_dropdown = driver.find_element(By.CSS_SELECTOR, 'a[class="jfHeader-menuListLink jfHeader-dynamicLink js-tracking"]')
# features_dropdown.click()
# time.sleep(1)
# integrations_dropdown = driver.find_element(By.CSS_SELECTOR, 'a[class="jfHeader-menuListLink jfHeader-dynamicLink js-tracking js-integrations"]')
# integrations_dropdown.click()
# time.sleep(1)
# company_dropdown = driver.find_element(By.CSS_SELECTOR, 'a[data-text-name="support"]')
# company_dropdown.click()
# time.sleep(1)

# # test inputs
# first_name1 = driver.find_element(By.CSS_SELECTOR, 'input[class="first_name input mb1"]')
# first_name1.send_keys("Halcyon")
# last_name1 = driver.find_element(By.CSS_SELECTOR, 'input[name="last_name"]')
# last_name1.send_keys("&on&on")
# business_name = driver.find_element(By.CSS_SELECTOR, 'input[name="business_name"]')
# business_name.send_keys("Orbital Enterprises")
# email_address = driver.find_element(By.CSS_SELECTOR, 'input[name="email"]')
# email_address.send_keys('turdman@fire.com')
# time.sleep(7)
# submit2_button = driver.find_element(By.CSS_SELECTOR, 'button[id="demo"]')
# submit2_button.click()
# time.sleep(3)
# signup_button = driver.find_element(By.CSS_SELECTOR, 'a[class="jfHeader-menuListLink jfHeader-dynamicLink jfHeader-signup-action signup  btn-outline-dark"]')
# signup_button.click()
# time.sleep(3)

# test signup: https://phptravels.org/register.php
driver.get('https://phptravels.org/register.php')
driver.maximize_window()
drop=Select(driver.find_element(By.CSS_SELECTOR, 'select[id="inputCountry"]'))
drop.select_by_visible_text('United States')
time.sleep(2)

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
time.sleep(3)

input_postcode = driver.find_element(By.CSS_SELECTOR, 'input[id="inputPostcode"]')
input_postcode.send_keys('78758')
time.sleep(1)

time.sleep(1)

time.sleep(3)
input_moblie = driver.find_element(By.CSS_SELECTOR, 'input[name="customfield[2]"]')
input_moblie.send_keys('1234567890')
input_password1 = driver.find_element(By.CSS_SELECTOR, 'input[name="password"]')
input_password1.send_keys('password84$')
input_password2 = driver.find_element(By.CSS_SELECTOR, 'input[name="password2"]')
input_password2.send_keys('password84$')
time.sleep(1)
# check_box = driver.find_element(By.CSS_SELECTOR, 'button[class="no-icheck toggle-switch-success"]').click()
# captcha_checkbox = driver.find_element(By.CSS_SELECTOR, 'input[id="recaptcha-anchor"]')
# captcha_checkbox.click()

time.sleep(3)


driver.quit()

