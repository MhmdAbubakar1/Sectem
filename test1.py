# driver = webdriver.Chrome()
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
user_name = "mabubakar/cui@gmail.com"
password = "DELLpc125"
driver = webdriver.Chrome()
driver.get("https://www.facebook.com")
element = driver.find_element_by_id("email")
element.send_keys(user_name)
element = driver.find_element_by_id("pass")
element.send_keys(password)
submit   = driver.find_element_by_id("loginbutton")
submit.click()
wait = WebDriverWait( driver, 5 )
page_title = driver.title
print(page_title)
assert page_title == "Facebook – log in or sign up"
# element.quit()
# element.send_keys(Keys.RETURN)
driver.close()