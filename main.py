import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By

user = 'rjlynch@btinternet.com'
password = ''

target_url = 'https://phoenixmmasouthampton.clubright.co.uk/Account/LogIn'

driver = webdriver.Chrome(r"/usr/lib/chromium-browser/chromedriver")

driver.get(target_url)

email_input = (By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[2]/div/div[2]/div/div/form/div[2]/div[1]/div/input')
email_btn = (By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[2]/div/div[2]/div/div/form/div[2]/div[2]/div/button')

WebDriverWait(driver, 10).until(EC.element_to_be_clickable(email_input)).send_keys(user)
time.sleep(5)
WebDriverWait(driver, 20).until(EC.element_to_be_clickable(email_btn)).click()

