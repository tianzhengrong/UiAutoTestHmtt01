from time import sleep
import page
from base.app_base import AppBase
from tools.get_log import GetLog

log = GetLog.get_logger()

class PageAppLogin(AppBase):
    # 今日头条app登录
    # 1. 点击 底部 未登录
    def page_click_nologin(self):
        self.base_click(page.app_nologin)

    # 2. 点击 红色登录按钮
    def page_click_redlogin(self):
        self.base_click(page.app_redlogin)

    # 3. 点击 底部 密码登录
    def page_click_codelogin(self):
        self.base_click(page.app_codelogin)

    # 4. 输入手机号
    def page_input_phone(self, phone):
        self.base_input(page.app_phone, phone)

    # 5. 输入密码
    def page_input_code(self, code):
        self.base_input(page.app_code, code)

    # 6. 点击 登录箭头
    def page_click_login_btn(self):
        sleep(2)
        self.base_click(page.app_login_btn)

    # 7. 判断页面是否存在 申请认证
    def page_is_login_success(self):
        return self.app_base_is_exist(page.app_request)

    # 8. 组合登录业务方法
    def page_app_login(self, phone, code):
        log.info("正在调用今日头条app登录业务方法， 手机号：{} 密码：{}".format(phone, code))
        self.page_click_nologin()
        self.page_click_redlogin()
        self.page_click_codelogin()
        self.page_input_phone(phone)
        self.page_input_code(code)
        self.page_click_login_btn()

    # 8. 组合登录成功业务方法
    def page_app_login_success(self, phone='18729399707', code='abc123'):
        log.info("正在调用今日头条app登录成功业务方法， 手机号：{} 密码：{}".format(phone, code))
        self.page_click_nologin()
        self.page_click_redlogin()
        self.page_click_codelogin()
        self.page_input_phone(phone)
        self.page_input_code(code)
        self.page_click_login_btn()