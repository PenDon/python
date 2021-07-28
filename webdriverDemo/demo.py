from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://www.baidu.com')
el = driver.find_elements_by_xpath('//div[@id="asdasdas"]')

print(el)

driver.close()