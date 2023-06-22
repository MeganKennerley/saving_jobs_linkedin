from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time
import os

chrome_driver_path = os.environ.get("chrome_driver_path")
service = Service(executable_path=chrome_driver_path)
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://www.linkedin.com/jobs/search/"
           "?currentJobId=3616386505&f_WT=2&geoId=102299470&keywords=python%20developer"
           "&location=England%2C%20United%20Kingdom&refresh=true")

sign_in = driver.find_element(by=By.LINK_TEXT, value="Sign in")
sign_in.click()

time.sleep(0.5)

email = driver.find_element(by=By.ID, value="username")
email.send_keys(os.environ.get("USERNAME"))

password = driver.find_element(by=By.ID, value="password")
password.send_keys(os.environ.get("PASSWORD"))

signin_button = driver.find_element(by=By.XPATH, value="//*[@id='organic-div']/form/div[3]/button")
signin_button.click()

time.sleep(1)

all_listings = driver.find_elements(by=By.CLASS_NAME, value="scaffold-layout__list-container")

for listing in all_listings:
    listing.click()
    time.sleep(2)

    try:
        save_button = driver.find_element(by=By.CLASS_NAME, value="jobs-save-button")
        save_button.click()
    except NoSuchElementException:
        print("skipped")
        continue

time.sleep(5)
driver.quit()