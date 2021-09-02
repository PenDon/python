from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from time import sleep
from icecream import ic
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

option = Options()
option.add_argument('--disable-blink-features=AutomationControlled')
driver = Chrome(options=option)

# driver.get("https://www.toutiao.com/")
driver.get("https://www.douyin.com/user/MS4wLjABAAAAvOU5GclmETa4jehXAEspnMfYJQZAbwcJzfUFhZk4cP8")

# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-title"))).click()
for i in range(30):
    a = 1000
    for j in range(10):
        v0 = a * j / 10
        if j < 5:
            distance = v0 * 0.1 + 1/2 * a * 0.01
        else:
            distance = v0 * 0.1 - 1/2 * a * 0.01

        ic(distance)
        driver.execute_script(f"window.scrollBy(0, {distance})")
        sleep(0.1)
    sleep(0.2)



# sleep(0.5)
#
#
#
# driver.execute_script("var action=document.documentElement.scrollTop=50000")
# sleep(0.5)
#
# driver.execute_script("var action=document.documentElement.scrollTop=50000")
# sleep(0.5)
#
# driver.execute_script("var action=document.documentElement.scrollTop=50000")
# sleep(0.5)
#
# driver.execute_script("var action=document.documentElement.scrollTop=50000")
# sleep(0.5)
#
# driver.execute_script("var action=document.documentElement.scrollTop=50000")
# sleep(0.5)

ul = driver.find_elements_by_xpath('//ul')[-1]

lis = ul.find_elements_by_xpath('./li')
ic(len(lis))
for li in lis:
    print(li.find_element_by_xpath('./a').get_attribute('href'))

driver.close()
