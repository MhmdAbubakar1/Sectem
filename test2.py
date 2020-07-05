# driver = webdriver.Chrome()
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome()

URL = "https://deeds.pk//products/al-smart-fit-cotton-side-stripes-black-shorts"
driver.get(URL)
inputElement1 = driver.find_element_by_id("quantity")
inputElement1.clear()
inputElement1.send_keys('100')
inputElement1.send_keys(Keys.RETURN)
# print(driver.current_url)


driver.get(driver.current_url)
clickButton = driver.find_element_by_id("checkout")
clickButton.send_keys(Keys.RETURN)
# print(driver.current_url)

driver.get(driver.current_url)
clickButton = driver.find_element_by_id("continue_button")
clickButton.send_keys(Keys.RETURN)
# print(driver.current_url)

driver.get(driver.current_url)
spanText = driver.find_element_by_class_name("product-thumbnail__quantity")
quantity = spanText.get_attribute('innerHTML')
print("Quantity=",quantity)