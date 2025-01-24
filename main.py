from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import os
import time
from time import sleep

from test import driver

# Tinder URL
TINDER = "https://tinder.com/"

# Facebook Credentials
EMAIL = os.environ.get('FACEBOOK_EMAIL')
PASSWORD = os.environ.get("FACEBOOK_PASSWORD")

# Keep Browser Window Open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(TINDER)

driver.maximize_window()

# TODO - Initial Login
time.sleep(2)
landing_page_login = driver.find_element(By.LINK_TEXT, "Log in")
landing_page_login.click()

# TODO - Facebook Login Sync
time.sleep(2)
facebook_login = driver.find_element(By.XPATH, '//*[@id="q369688754"]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]/div[2]/div/div')
facebook_login.click()

time.sleep(2)

# TODO - Get all windows
handles = driver.window_handles

# TODO - print(handles)
base_window = handles[0]
fb_login_window = handles[1]

# TODO - print(fb_login_window)
driver.switch_to.window(fb_login_window)

print(driver.title)

# TODO - Signing in through Facebook
time.sleep(2)
email = driver.find_element(By.XPATH, '//*[@id="email"]')
email.send_keys(EMAIL, Keys.ENTER)
password = driver.find_element(By.XPATH, '//*[@id="pass"]')
password.send_keys(PASSWORD, Keys.ENTER)

print(driver.title)

# TODO - Continue as Corey
time.sleep(2)
continue_as_corey = driver.find_element(By.CSS_SELECTOR, value="div[aria-label='Continue as Corey']")
time.sleep(2)
continue_as_corey.click()

driver.switch_to.window(base_window)

# # TODO - Tinder Cookie Accept Button
time.sleep(2)
accept = driver.find_element(By.XPATH, '//*[@id="q369688754"]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]/div')
accept.click()

# TODO - Allow Location
time.sleep(2)
allow = driver.find_element(By.XPATH, '//*[@id="q369688754"]/div/div/div/div/div[3]/button[1]')
allow.click()

# TODO - Do Not Notify Me
time.sleep(2)
notify = driver.find_element(By.XPATH, '//*[@id="q369688754"]/div/div/div/div/div[3]/button[2]')
notify.click()

# TODO - See Who Likes You
time.sleep(2)
maybe_later = driver.find_element(By.XPATH, '//*[@id="q369688754"]/div/div/div/div[3]/button[2]')
maybe_later.click()

# TODO - Swiping
for n in range(100):

    # 1-Second delay in between likes
    time.sleep(1)

    try:
        print("called")
        like_button = driver.find_element(By.XPATH, '//*[@id="main-content"]/div[2]/div/div/div/div[1]/div/div/div[4]/div/div[4]/button')
        like_button.click()

    except ElementClickInterceptedException:
        try:
            match = driver.find_element(By.CSS_SELECTOR, '.itsAMatch a')
            match.click()

        except NoSuchElementException:
            sleep(2)

driver.quit()
