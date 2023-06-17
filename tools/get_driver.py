from time import sleep

from selenium import webdriver
import appium.webdriver

import page


class GetDriver:
    # 1.声明变量
    __web_driver = None

    # 声明app中driver变量
    __app_driver = None

    # 2.获取driver方法
    @classmethod
    def get_web_driver(cls, url):
        # 判断是否为空
        if cls.__web_driver is None:
            # 获取浏览器
            cls.__web_driver = webdriver.Chrome()
            # 最大化浏览器
            cls.__web_driver.maximize_window()
            # 打开url
            cls.__web_driver.get(url)
        # 返回driver
        return cls.__web_driver

    # 3.退出driver方法
    @classmethod
    def quit_web_driver(cls):
        # 判断driver不为空
        if cls.__web_driver:
            # 退出操作
            cls.__web_driver.quit()
            # 置空操作 重点
            cls.__web_driver = None

    # 获取app应用driver
    @classmethod
    def get_app_driver(cls):
        # 判断 __app_driver 为空
        if cls.__app_driver is None:
            # 设置启动
            desired_caps = {}
            # 必填-且正确
            desired_caps['platformName'] = 'Android'
            # 必填-且正确
            desired_caps['platformVersion'] = '7'
            # 必填
            desired_caps['deviceName'] = 'emulator-5554'
            # APP包名
            desired_caps['appPackage'] = page.appPackage
            # 启动名
            desired_caps['appActivity'] = page.appActivity
            # windows注意输入键盘编码
            desired_caps['unicodeKeyboard'] = True
            desired_caps['resetKeyboard'] = True
            # 设置driver
            cls.__app_driver = appium.webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
            # print(desired_caps)

        # 返回cls.__app_driver
        return cls.__app_driver
        pass

    # 退出app应用driver
    @classmethod
    def quit_app_driver(cls):
        # 判断不为空
        if cls.__app_driver:
            # 退出操作
            cls.__app_driver.quit()
            # 置空操作
            cls.__app_driver = None

if __name__ == '__main__':
    GetDriver.get_app_driver()
    sleep(2)
    GetDriver.quit_app_driver()