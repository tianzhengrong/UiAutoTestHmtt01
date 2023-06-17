import page
from page.page_in import PageIn
from tools.get_driver import GetDriver


class TestMpOrder:
    # 1.初始化
    def setup_class(self):
        # 1.获取driver
        driver = GetDriver.get_web_driver(page.url_houtai)
        # 2.获取统一入口类
        self.page_in = PageIn(driver)
        # 3.调用成功登录依赖方法
        self.page_in.page_get_PageMpLogin().page_mp_login_sucsess()
        # 4.获取PageMpOrder对象
        self.mporder = self.page_in.page_get_PageMpOrder()

    # 2.结束
    def teardown_class(self):
        # 关闭driver
        GetDriver.quit_web_driver()

    # 3.tpshop购买商品业务测试方法
    def test_tpshop_order(self, shopname='手机'):
        """想要获取后台订单号，与前端生成的订单号进行对比"""
        # 调用后台订单业务方法
        self.mporder.page_mp_order()
        self.mporder.web_base_is_exist(self.mporder.houtai_ordernumber)