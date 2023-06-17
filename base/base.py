import os
import allure
from selenium.webdriver.support.wait import WebDriverWait
from config import BASE_PATH
from tools.get_log import GetLog

log = GetLog.get_logger()

class Base:

    # 初始化
    def __init__(self, driver):
        log.info("正在初始化driver：{}".format(driver))
        """解决driver"""
        self.driver = driver

    # 查找 方法封装
    def base_find(self, loc, timeout=30, poll=0.5):
        """

        :param loc:格式为列表或元组，内容：元素定位信息使用By类
        :param timeout: 查找元素超时时间，默认30秒
        :param poll: 查找元素频率，默认为0.5
        :return: 元素
        """
        log.info("正在查找元素：{}".format(loc))
        return (WebDriverWait(self.driver,
                              timeout=timeout,
                              poll_frequency=poll).until(lambda x: x.find_element(*loc)))

    # 输入 方法封装
    def base_input(self, loc, value):
        """
        :param loc:元素的定位信息
        :param value: 要输入的值
        """
        # 1.获取元素
        el = self.base_find(loc)
        # 2.清空操作
        log.info("正在对：{}元素执行清空操作！".format(loc))
        el.clear()
        # 3.输入操作
        log.info("正在对：{}元素执行输入：{}操作！".format(loc,value))
        el.send_keys(value)

    # 点击 方法封装
    def base_click(self, loc):
        """
        :param loc: 元素的定位信息
        """
        log.info("正在对：{}元素执行点击操作！".format(loc))
        self.base_find(loc).click()

    # 获取 元素文本
    def base_get_text(self, loc):
        """
        :param loc: 元素的定位信息
        :return: 返回元素的文本值
        """
        log.info("正在对：{}元素获取文本操作，获取的文本值：{}".format(loc,self.base_find(loc).text))
        return self.base_find(loc).text

    # 截图
    def base_get_img(self):
        # 1.调用截图方法
        log.error("断言出错，正在执行截图操作！")
        img_name = BASE_PATH + os.sep + "image" + os.sep + "err.png"
        self.driver.get_screenshot_as_file(img_name)
        # 2.调用图片写入报告方法
        log.error("断言出错，正在将错误图片写入allure报告！")
        self.__base_write_img(img_name)

    # 将图片写入报告 方法 （私有）
    def __base_write_img(self, img_name):
        # 1.获取图片文件流
        with open(img_name, "rb")as f:
            # 2.调用allure.attach附加方法
            allure.attach(f.read(), "断言失败", allure.attachment_type.PNG)

