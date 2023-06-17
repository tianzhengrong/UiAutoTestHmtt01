from time import sleep
import page
from base.web_base import WebBase

class PageMpOrder(WebBase):
    houtai_ordernumber = None
    # 点击 系统
    def page_click_system(self):
        sleep(1)
        self.base_click(page.mp_system)

    # 点击 清除缓存
    def page_click_clearcache(self):
        sleep(0.5)
        self.base_click(page.mp_clearcache)

    # 点击 待处理订单
    def page_click_order(self):
        sleep(0.5)
        # 1.切换iframe1
        iframe1 = self.base_find(page.mp_iframe1)
        self.driver.switch_to.frame(iframe1)
        # 2.点击待处理订单
        self.base_click(page.mp_order)

    # 获取 订单列表的第一个订单号
    def page_get_ordernumber(self):
        return self.base_get_text(page.mp_ordernumber)

    # 组合获取后台订单号业务方法
    def page_mp_order(self):
        self.page_click_system()
        self.page_click_clearcache()
        self.page_click_order()
        self.houtai_ordernumber = self.page_get_ordernumber()
        print("后台获取的订单号为：", self.houtai_ordernumber)
