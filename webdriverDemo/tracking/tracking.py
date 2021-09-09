from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

tracking_number = "CMAU8282380"

driver = webdriver.Chrome()
driver.get("http://www.cma-cgm.com/ebusiness/tracking")
# WebDriverWait(driver, 3).until(ec.visibility_of_element_located((By.ID, "Reference")))
# WebDriverWait(driver, 3).until(ec.element_to_be_clickable((By.ID, "btnTracking")))
input_element = driver.find_element(By.ID, "Reference")
search_button = driver.find_element(By.ID, "btnTracking")
input_element.send_keys(tracking_number)
search_button.click()

WebDriverWait(driver, 3).until(ec.visibility_of_element_located((By.TAG_NAME, "tr")))
driver.save_screenshot("search.png")
driver.close()
