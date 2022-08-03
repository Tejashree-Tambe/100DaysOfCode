from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\Development\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get("https://www.python.org/")

# # To get element by id:
# navbar = driver.find_element_by_id("top")
# print(navbar.text)

# # To get element by name:
# search_bar = driver.find_element_by_name("q")
# print(search_bar.text)
# print(search_bar.get_attribute("placeholder"))

# # To get element by class:
# logo = driver.find_element_by_class_name("python-logo")
# print(logo.size)

# # To get element by css_file selector:
# docs_link = driver.find_element_by_css_selector(".documentation-widget a")
# print(docs_link.text)

# # To get element by xpath:
# py_version = driver.find_element_by_xpath('//*[@id="content"]/div/section/div[1]/div[2]/p[2]/a')
# print(py_version.text)

# # Events
# event_dates = driver.find_elements_by_css_selector(".event-widget time")
# event_names = driver.find_elements_by_css_selector(".event-widget li a")
# events = {}
#
# for i in range(len(event_names)):
#     event_details = {
#         "time": event_dates[i].text,
#         "name": event_names[i].text,
#     }
#     events[i] = event_details
#
# print(events)
# driver.quit()

# Wikipedia
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
#
# no_of_articles = driver.find_element_by_css_selector("#articlecount a")

# # click a link/button
# no_of_articles.click()

# all_portals = driver.find_element_by_link_text("All portals")
# all_portals.click()

# # type in elements
# search = driver.find_element_by_name("search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

# Signing up
driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element_by_name("fName")
first_name.send_keys("Python")

last_name = driver.find_element_by_name("lName")
last_name.send_keys("Developer")

email = driver.find_element_by_name("email")
email.send_keys("example@gmail.com")

button = driver.find_element_by_class_name("btn-primary")
button.click()
