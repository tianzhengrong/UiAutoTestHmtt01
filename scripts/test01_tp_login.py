import pytest
import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLog
from tools.read_yaml import read_yaml
log = GetLog.get_logger()

class TestTpLogin:
    # 初始化
    def setup_class(self):
        # 1.获取driver
        driver = GetDriver.get_web_driver(page.url_mp)
        # 2.通过统一入口类获取PageMpLogin对象
        self.mp = PageIn(driver).page_get_PageTpLogin()

    # 结束
    def teardown_class(self):
        # 调用关闭driver
        GetDriver.quit_web_driver()

    # 测试业务方法
    @pytest.mark.parametrize("username,password,code,expect", read_yaml("tp_login.yaml"))
    def test_mp_login(self, username, password, code, expect):
        # 调用登录业务方法
        self.mp.page_tp_login(username=username, password=password, code=code)
        try:
            assert expect == self.mp.page_get_nickname()
        except Exception as e:
            # 输出错误信息
            log.error("断言出错，错误信息：{}".format(e))
            print("断言失败：", e)
            # 截图
            self.mp.base_get_img()
            # 抛出异常
            raise


