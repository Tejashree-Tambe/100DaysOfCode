from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PINCODE = 400104

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.dmart.in/")

time.sleep(2)
# Give Pincode and confirm
pincode_input = driver.find_element_by_id("pincodeInput")
pincode_input.send_keys(PINCODE)
time.sleep(3)
pincodes = driver.find_elements_by_xpath('/html/body/div[2]/div[3]/div/div[2]/div/div/div[2]/div/ul/li/button')
# selecting the pincode
for click_pincode in pincodes:
    click_pincode.click()
# clicking on start shopping button
start_button = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div[2]/div/div/div[3]/div/div[2]/div[2]/button')
start_button.click()

time.sleep(2)

# Searching products
search = driver.find_element_by_class_name("src-client-components-header-components-search-__search-module___searchInput")
search.send_keys("Amul Butter 500g")
search.send_keys(Keys.ENTER)

time.sleep(3)

add_cart = driver.find_element_by_class_name("src-client-components-product-card-cart-action-__cart-action-module___action")
add_cart.click()


