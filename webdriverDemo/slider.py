# _*_coding:utf-8_*_
# 作者         ：Seyo
# 创建时间     ：2019/10/18 16:14
# IDE          ：PyCharm

# 模拟登陆 - 破除滑动验证

from io import BytesIO
from selenium import webdriver
from selenium.webdriver import ActionChains
import time
from PIL import Image
import random

url = 'https://passport.bilibili.com/login'
browser = webdriver.Chrome()


def compare_pixel(image1, image2, i, j):
    """
    判断两个像素是否相同
    :param image1: 图片1
    :param image2: 图片2
    :param i:
    :param j:
    :return:
    """
    pixel1 = image1.load()[i, j]
    pixel2 = image2.load()[i, j]
    threshold = 60  # 设置一个比较基准

    if abs(pixel1[0] - pixel2[0]) < threshold and abs(pixel1[1] - pixel2[1]) < threshold and abs(
            pixel1[2] - pixel2[2]) < threshold:
        return True
    else:
        return False


def update_style(display):
    """
        修改图片的style属性，
    """
    js = 'document.querySelectorAll("canvas")[3].style="display:{display}"'.format(display=display)
    browser.execute_script(js)
    time.sleep(2)


def crop_image(image_file_name):
    time.sleep(2)
    # 截取验证码图片
    img = browser.find_element_by_xpath("//*[@class='geetest_canvas_slice geetest_absolute']")
    location = img.location
    print("图片的位置", location)
    size = img.size
    print(size)
    top, button, left, right = location['y'], location['y'] + size['height'], location['x'], location['x'] + size[
        'width']
    print("验证码位置", left, top, right, button)
    # 截图为png格式
    screenshot = browser.get_screenshot_as_png()
    # 转换为BytesIO能够让Image.open识别
    screenshot = Image.open(BytesIO(screenshot))
    # 截取图片
    captcha = screenshot.crop((int(left), int(top), int(right), int(button)))
    # 保存
    captcha.save(image_file_name)
    return captcha


def login():
    username = "123456"
    password = "131313"
    browser.get(url)
    browser.maximize_window()  # 全屏

    username_ele = browser.find_element_by_xpath("//input[@id='login-username']")
    password_ele = browser.find_element_by_xpath("//input[@id='login-passwd']")
    submit = browser.find_element_by_xpath("//a[@class='btn btn-login']")
    username_ele.send_keys(username)
    password_ele.send_keys(password)
    submit.click()
    time.sleep(2)
    # 鼠标移动到正确元素上
    slider = browser.find_element_by_xpath("//div[@class='geetest_slider_button']")

    # 获取缺口图片
    image1 = crop_image("captchal.png")
    # 显示没有缺口的图片
    update_style('block')
    # 获取完整图片
    time.sleep(1)
    image2 = crop_image("captchal1.png")
    # 修改回又缺口的图片
    update_style('none')
    left = 53
    has_find = False
    for i in range(left, image1.size[0]):
        if has_find:
            break
        for j in range(image1.size[1]):
            # 两张图片进行对比，（i,j）像素点的RGB差距，过大则x为偏移量
            if not compare_pixel(image1, image2, i, j):
                left = i
                has_find = True
                break
    left -= 6
    print("left", left)
    # 拖动图片
    # 根据偏移量获取移动轨迹
    # 一开始加速,然后减速，生长曲线，且加入点随机变动
    # 移动轨迹

    # track = []
    # # 当前位移
    #
    # current = 0
    # # 减速阈值
    #
    # mid = int(left * 3 / 5)
    # # 设置时间间隔
    # t = 0.2
    # # 设置初速度
    #
    # v = 0
    # # 循环直到滑动到偏移值时退出
    # while current < left:
    #     # 根据是否临界点改变运动状态
    #     if current < mid:
    #         # 加速度
    #         a = random.randint(2, 3)
    #     else:
    #         a = -random.randint(6, 7)
    #     v0 = v
    #
    #     # 当前速度
    #     v = v0 + a * t
    #
    #     # 移动距离
    #     move = v0 * t + 0.5 * a * t * t
    #
    #     # 当前位移
    #     current += move
    #
    #     track.append(round(move))
    #
    # 点击拖动按钮
    track = [round(0.6 * left), round(0.3 * left), round(0.1 * left)]
    print(track)
    ActionChains(browser).click_and_hold(slider).perform()
    for x in track:
        # 开始拖动
        ActionChains(browser).move_by_offset(xoffset=x, yoffset=0).perform()
        time.sleep(0.5)
    # 松开按钮
    ActionChains(browser).release().perform()
    time.sleep(10)


login()
time.sleep(10)
browser.quit()
