import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome()

URL = "https://deeds.pk//products/al-smart-fit-cotton-side-stripes-black-shorts.json"
driver.get(URL)

element = driver.find_element_by_tag_name("pre")
all_json_data = json.loads(element.get_attribute('innerHTML'))
variants = all_json_data["product"]["variants"]

variant_ids = []
variant_option2 = []
string_variant_ids = []
for variant in variants:
	variant_ids.append(variant["id"])
	variant_option2.append(variant["option2"])
	string_variant_ids.append(str(variant["id"]))

def quantity_finder(id):
	id_URL = "https://deeds.pk//products/al-smart-fit-cotton-side-stripes-black-shorts?variant=" + id
	driver.get(id_URL)
	sold_out_element = driver.find_element_by_class_name("sold_out")
	sold_out_class_text = sold_out_element.get_attribute('innerHTML')
	if (sold_out_class_text == "Sold Out"):
		quantity = 0
		return quantity

	inputElement1 = driver.find_element_by_id("quantity")
	inputElement1.clear()
	inputElement1.send_keys('100')
	inputElement1.send_keys(Keys.RETURN)

	driver.get(driver.current_url)
	clickButton = driver.find_element_by_id("checkout")
	clickButton.send_keys(Keys.RETURN)

	driver.get(driver.current_url)
	clickButton = driver.find_element_by_id("continue_button")
	clickButton.send_keys(Keys.RETURN)

	driver.get(driver.current_url)
	spanText = driver.find_element_by_class_name("product-thumbnail__quantity")
	quantity = spanText.get_attribute('innerHTML')

	return int(quantity)

quantities = []

for string_variant_id in string_variant_ids:
	quantity = quantity_finder(string_variant_id)
	quantities.append(quantity)

for i in range(len(variants)):
	print(variant_option2[i] + '-->  ', quantities[i])