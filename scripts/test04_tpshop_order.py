from time import sleep

import page
from page.page_in import PageIn
from tools.get_driver import GetDriver


class TestTpshopOrder:
    # 1.初始化
    def setup_class(self):
        # 1.获取driver
        driver = GetDriver.get_web_driver(page.url_mp)
        # 2.获取统一入口类
        self.page_in = PageIn(driver)
        # 3.调用成功登录依赖方法
        self.page_in.page_get_PageTpLogin().page_tp_login_success()
        # 4.获取PageTpshopOrder对象
        self.tpshop = self.page_in.page_get_PageTpshopOrder()
        # 5.获取PageMpOrder对象
        self.houtai_order = self.page_in.page_get_PageMpOrder()

    # 2.结束
    def teardown_class(self):
        # 关闭driver
        GetDriver.quit_web_driver()

    # 3.tpshop购买商品业务测试方法
    def test_tpshop_order(self, shopname='手机'):
        # 调用购买商品业务方法
        self.tpshop.page_tpshop_order(shopname)