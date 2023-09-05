from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
import time

s = Service('/home/metranohm/seleniumdrivers/chromedriver')
driver = webdriver.Chrome(service=s)
driver.get('https://andrew-winkler-portfolio.netlify.app/')
driver.maximize_window()
time.sleep(2)

about_link = driver.find_element(By.CSS_SELECTOR, 'a[id="about-navLink"]')
about_link.click()

time.sleep(1)

contact_link = driver.find_element(By.CSS_SELECTOR, 'a[id="contact-navLink"]')
contact_link.click()

time.sleep(1)

resume_link = driver.find_element(By.CSS_SELECTOR, 'a[id="resume-navLink"]')
resume_link.click()

time.sleep(1)

projects_link = driver.find_element(By.CSS_SELECTOR, 'a[id="projects-navLink"]')
projects_link.click()

time.sleep(1)

filmingo_click = driver.find_element(By.CSS_SELECTOR, 'a[href="/projects/filmingo---fantasy-filmmaking"]')
filmingo_click.click()
time.sleep(1)

filmingo_goback = driver.find_element(By.CSS_SELECTOR, 'a[href="/projects"]')
filmingo_goback.click()

time.sleep(1)

finch_click = driver.find_element(By.CSS_SELECTOR, 'a[href="/projects/finch-collector"]')
finch_click.click()

time.sleep(1)

finch_goback = driver.find_element(By.CSS_SELECTOR, 'a[href="/projects"]')
finch_goback.click()

time.sleep(1)

password_generator_click = driver.find_element(By.CSS_SELECTOR, 'a[href="/projects/js-password-generator"]')
password_generator_click.click()

time.sleep(1)

password_generator_back = driver.find_element(By.CSS_SELECTOR, 'a[href="/projects"]')
password_generator_back.click()

time.sleep(1)

austinmusic_click = driver.find_element(By.CSS_SELECTOR, 'a[href="/projects/austin-music-underground"]')
austinmusic_click.click()

time.sleep(1)

music_back = driver.find_element(By.CSS_SELECTOR, 'a[href="/projects"]')
music_back.click()

time.sleep(1)

calculator_click = driver.find_element(By.CSS_SELECTOR, 'a[href="/projects/react-calculator"]')
calculator_click.click()

time.sleep(1)

calculator_back = driver.find_element(By.CSS_SELECTOR, 'a[href="/projects"]')
calculator_back.click()

time.sleep(1)

weather_click = driver.find_element(By.CSS_SELECTOR, 'a[href="/projects/weather-tracker"]')
weather_click.click()

time.sleep(1)

weather_back = driver.find_element(By.CSS_SELECTOR, 'a[href="/projects"]')
weather_back.click()

time.sleep(1)

candy_click = driver.find_element(By.CSS_SELECTOR, 'a[href="/projects/museum-of-candy"]')
candy_click.click()

time.sleep(1)

candy_back = driver.find_element(By.CSS_SELECTOR, 'a[href="/projects"]')
candy_back.click()

time.sleep(1)

connect_click = driver.find_element(By.CSS_SELECTOR, 'a[href="/projects/connect-four"]')
connect_click.click()

time.sleep(1) 

connect_back = driver.find_element(By.CSS_SELECTOR, 'a[href="/projects"]')
connect_back.click()

home_end = driver.find_element(By.CSS_SELECTOR, 'a[class="NavBar_name__ZPtL0"]')
home_end.click()

time.sleep(3)

driver.quit()