from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


EMAIL = "email"
PASSWORD = "password"

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://twitter.com/home")
driver.maximize_window()

time.sleep(5)
email = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
email.send_keys(EMAIL)

password = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)

time.sleep(10)
tweet_button = driver.find_element_by_link_text("Tweet")
tweet_button.click()
#

time.sleep(40)
msg = "Hello, Testing Web Scraping via Selenium"

tweet_click = driver.find_element_by_class_name("DraftEditor-root")
tweet_click.click()

tweet = driver.find_element_by_class_name("public-DraftEditorPlaceholder-root")
tweet.send_keys(msg)

tweet_confirm = driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]')
tweet_confirm.click()
