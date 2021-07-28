from io import BytesIO
from selenium import webdriver
from selenium.webdriver import ActionChains
import time
from PIL import Image

# 尝试模拟图片滑动验证

class Login:
    url = 'https://passport.bilibili.com/login'
    username = "xxx"
    password = "xxx"
    img1 = "img1.png"
    img2 = "img2.png"

    def __init__(self):
        option = webdriver.ChromeOptions()
        option.add_argument('--user-data-dir=C:\\Users\Administrator\AppData\Local\Google\Chrome\\User')
        self.driver = webdriver.Chrome(options=option)
        pass

    def getPage(self):
        self.driver.get(self.url)
        self.driver.maximize_window() # 最大化窗口
        pass

    def sendKeys(self):
        user = self.driver.find_element_by_xpath('//input[@id="login-username"]')
        pwd = self.driver.find_element_by_xpath('//input[@id="login-passwd"]')
        login = self.driver.find_element_by_xpath('//a[contains(@class, "login")]')
        user.send_keys(self.username)
        pwd.send_keys(self.password)
        login.click()

    def getImg(self, filename):
        time.sleep(2)
        img = self.driver.find_element_by_xpath("//*[@class='geetest_canvas_slice geetest_absolute']")
        location = img.location
        size = img.size
        top, bottom, left, right = location['y'], location['y'] + size['height'], location['x'], location['x'] + size['width']
        screenShot = self.driver.get_screenshot_as_png()
        screenShot = Image.open(BytesIO(screenShot))
        img = screenShot.crop((int(left), int(top), int(right), int(bottom)))
        img.save(filename)

    def jsExecute(self,display):
        js = f'document.querySelectorAll("canvas")[3].style="display:{display}"'
        self.driver.execute_script(js)

    def imgCompare(self):
        t = 60
        location = []
        img1 = Image.open(self.img1, "r")
        img2 = Image.open(self.img2, "r")
        pix1 = img1.load()
        pix2 = img2.load()
        for i in range(img1.size[0]):
            for j in range(img1.size[1]):
                if abs(pix1[i, j][1] - pix2[i, j][1]) > t or abs(pix1[i, j][0] - pix2[i, j][0]) > t or abs(pix1[i, j][2] - pix2[i, j][2]) > t:
                    location.append(i)
                else:
                    continue
        for e in location:
            if e > location[0] + 50:
                location = [location[0], e]
                break
            else:
                continue
        print("find", location)
        return location[1] - location[0]

    def dragSlider(self, dist):
        track = [round(0.4 * dist), round(0.3 * dist), round(0.2 * dist), round(0.1 * dist)]
        slider = self.driver.find_element_by_xpath('//div[@class="geetest_slider_button"]')
        ActionChains(self.driver).click_and_hold(slider).perform()
        for index, l in enumerate(track):
            ActionChains(self.driver).move_by_offset(l, 0).perform()
            if index != len(track) - 1:
                time.sleep(0.1)
        ActionChains(self.driver).release(slider).perform()

    def run(self):
        self.getPage()
        self.sendKeys()
        self.getImg(self.img1)
        self.jsExecute("block")
        self.getImg(self.img2)
        dist = self.imgCompare()
        self.dragSlider(dist)

        time.sleep(10)
        self.driver.quit()

start = time.time()
login = Login()
try:
    login.run()
except Exception as e:
    print(e)
    login.driver.quit()
end = time.time()
print(f"总用时{end - start}s")

