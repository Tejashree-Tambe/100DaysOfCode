from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&geoId=102713980&keywords=python%20developer&location=India")

EMAIL_ID = "email"
PASSWORD = "password"
PHONE_NO = "8745232254"

# search_job_type = driver.find_element_by_id("jobs-search-box__text-input jobs-search-box__keyboard-text-input jobs-search-box__ghost-text-input")
# print(search_job_type.get_attribute("placeholder"))

signup = driver.find_element_by_link_text("Sign in")
signup_page = signup.click()

username = driver.find_element_by_id("username")
username.send_keys(EMAIL_ID)

password = driver.find_element_by_id("password")
password.send_keys(PASSWORD)

signup_button = driver.find_element_by_class_name("btn__primary--large")
signup_button.click()

jobs = driver.find_elements_by_css_selector(".jobs-search-results__list .flex-grow-1 a")

for job in jobs:
    job.click()

    try:
        apply = driver.find_element_by_class_name("jobs-s-apply button")
        apply.click()

        phone = driver.find_element_by_class_name("fb-single-line-text__input")
        if phone.text == "":
            phone.send_keys(PHONE_NO)

        submit_button = driver.find_element_by_css_selector("footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()

            cancel_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
            cancel_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()

        close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        print("Application Button unavailable")
