import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By

# credential variables
user = 'rjlynch@btinternet.com'
password = 'Chico18069'

target_url = 'https://phoenixmmasouthampton.clubright.co.uk/Account/LogIn'

# web driver
driver = webdriver.Chrome(r"/usr/lib/chromium-browser/chromedriver")
driver.get(target_url)

# element variables
email_input = (By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[2]/div/div[2]/div/div/form/div[2]/div[1]/div/input')
driver.execute_script("window.scrollTo(0, 500)")
email_btn = (By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[2]/div/div[2]/div/div/form/div[2]/div[2]/div/button')
password_input = (By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[2]/div/div[2]/div/div/form/div[2]/div[1]/div/input[2]')
password_btn = (By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[2]/div/div[2]/div/div/form/div[2]/div[2]/div/button')
booking_btn = (By.XPATH, '/html/body/div[1]/div/div[2]/div/div[1]/div[2]/div/div/div[2]/div[6]/div/a/div')
activities_acc = (By.XPATH, '/html/body/div[1]/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/div[1]/button')
bjj_btn = (By.XPATH, '/html/body/div[1]/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/div[1]/div/div/div[5]/div')

# enter email
WebDriverWait(driver, 10).until(EC.element_to_be_clickable(email_input)).send_keys(user)

# sleep to enable element to show
time.sleep(5)

# click email button
WebDriverWait(driver, 20).until(EC.element_to_be_clickable(email_btn)).click()

# enter password
WebDriverWait(driver, 10).until(EC.element_to_be_clickable(password_input)).send_keys(password)

# sleep to enable element to show
time.sleep(5)

# click password btn
WebDriverWait(driver, 20).until(EC.element_to_be_clickable(password_btn)).click()

# click make booking
WebDriverWait(driver, 10).until(EC.element_to_be_clickable(booking_btn)).click()

# click activities accordian
WebDriverWait(driver, 10).until(EC.element_to_be_clickable(activities_acc)).click()

# click bjj gi / no gi button
WebDriverWait(driver, 10).until(EC.element_to_be_clickable(bjj_btn)).click()
