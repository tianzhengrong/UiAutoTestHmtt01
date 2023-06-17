from time import sleep
import page
from base.web_base import WebBase
from tools.get_log import GetLog

log = GetLog.get_logger()

class PageTpLogin(WebBase):
    # 输入用户名
    def page_inout_username(self, username):
        # 调用父类中输入方法
        self.base_input(page.tp_username, username)

    # 输入密码
    def page_input_password(self, password):
        # 调用父类中输入方法
        self.base_input(page.tp_passward, password)

    # 输入验证码
    def page_input_code(self, code):
        # 调用父类中输入方法
        self.base_input(page.tp_code, code)

    # 点击登录按钮
    def page_click_login_btn(self):
        sleep(1)
        # 调用父类中点击方法
        self.base_click(page.tp_login_btn)
        sleep(1)

    # 获取昵称 -> 测试脚本层断言使用
    def page_get_nickname(self):
        # 调用父类中 获取文本方法
        return self.base_get_text(page.tp_nickname)

    # 组合业务 -> tpshop前端登录依赖使用
    def page_tp_login(self, username, password, code):
        log.info("正在调用tpshop前端登录业务方法，用户名：{} 密码：{}".format(username, password))
        self.page_inout_username(username)
        self.page_input_password(password)
        self.page_input_code(code)
        self.page_click_login_btn()

    # 组合业务 -> tpshop前端成功登录依赖使用
    def page_tp_login_success(self, username='18729399707', password='abc123', code='8888'):
        log.info("正在调用tpshop前端成功登录业务方法，用户名：{} 密码：{}".format(username, password))
        self.page_inout_username(username)
        self.page_input_password(password)
        self.page_input_code(code)
        self.page_click_login_btn()