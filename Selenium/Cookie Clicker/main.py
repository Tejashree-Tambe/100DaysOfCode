from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie_area = driver.find_element_by_id("cookie")

items = driver.find_elements_by_css_selector("#store div")
item_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 5
five_min = time.time() + 60*5

while True:
    cookie_area.click()

    if time.time() > timeout:
        right_panel = driver.find_elements_by_css_selector("#store b")
        cookies_needed_to_level_up = []

        for cookie in right_panel:
            if cookie.text != "":
                cookies_needed = int(cookie.text.split("-")[1].strip().replace(",", ""))
                cookies_needed_to_level_up.append(cookies_needed)

        cookie_upgrades = {}
        for n in range(len(cookies_needed_to_level_up)):
            cookie_upgrades[cookies_needed_to_level_up[n]] = item_ids[n]

        cookies_earned = driver.find_element_by_id("money").text
        if "," in cookies_earned:
            cookies_earned = int(cookies_earned.replace(",", ""))

        else:
            cookies_earned = int(cookies_earned)

        affordable_upgrades = {}
        for cookies_needed, id in cookie_upgrades.items():
            if cookies_needed < cookies_earned:
                affordable_upgrades[cookies_needed] = id

        highest_affordable_upgrade = max(affordable_upgrades)
        to_purchase_id = affordable_upgrades[highest_affordable_upgrade]

        driver.find_element_by_id(to_purchase_id).click()

        timeout = time.time() + 5

    if time.time() > five_min:
        cookie_per_s = driver.find_element_by_id("cps").text
        print(cookie_per_s)
        break
