import pytest
import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLog
from tools.read_yaml import read_yaml

log = GetLog.get_logger()

class TestMpLogin:
    # 初始化
    def setup_class(self):
        # 1.获取driver
        driver = GetDriver.get_web_driver(page.url_houtai)
        # 2.通过统一入口类获取PageMpLogin对象
        self.login = PageIn(driver).page_get_PageMpLogin()

    # 结束
    def teardown_class(self):
        # 调用关闭driver
        GetDriver.quit_web_driver()

    # 测试业务方法
    @pytest.mark.parametrize("username, password, code, expect", read_yaml("mp_login.yaml"))
    def test_mp_login(self, username, password, code, expect):
        # 1.调用登录业务方法
        self.login.page_mp_login(username, password, code)

        try:
            # 2.调试断言信息
            assert expect == self.login.page_get_nickname()
        except Exception as e:
            # 日志
            log.error(e)
            # 截图
            self.login.base_get_img()
            # 抛异常
            raise