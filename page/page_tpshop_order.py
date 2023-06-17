from time import sleep

from base.web_base import WebBase
import page

class PageTpshopOrder(WebBase):
    ordernumber = None
    # 点击 首页
    def page_click_homepage(self):
        sleep(1)
        self.base_click(page.tpshop_homepage)

    # 点击 搜索框
    def page_click_search(self):
        sleep(1)
        self.base_click(page.tpshop_search)

    # 输入 购买商品名称
    def page_input_shopname(self, shopname):
        sleep(1)
        self.base_input(page.tpshop_search, shopname)

    # 点击 搜索按钮
    def page_click_search_btn(self):
        sleep(1)
        self.base_click(page.tpshop_search_btn)

    # 点击 加入购物车
    def page_click_addshopcar(self):
        sleep(1)
        self.base_click(page.tpshop_addshopcar)

    # 点击 立即购买
    def page_click_buy(self):
        sleep(1)
        self.base_click(page.tpshop_buy)

    # 点击 提交订单
    def page_click_submitorder(self):
        sleep(1)
        self.base_click(page.tpshop_submitorder)

    """获取订单号方法 结果为 订单：202306142123014673"""
    # 点击 订单详情
    def page_click_orderdetail(self):
        sleep(1)
        self.base_click(page.tpshop_orderdetail)
    # 获取 订单号
    def page_get_ordernumber(self):
        sleep(1)
        return self.base_get_text(page.tpshop_ordernumber)

    # 组合购买物品业务方法
    def page_tpshop_order(self, shopname):
        self.page_click_homepage()
        self.page_click_search()
        self.page_input_shopname(shopname)
        self.page_click_search_btn()
        self.page_click_addshopcar()
        self.page_click_buy()
        self.page_click_submitorder()
        self.page_click_orderdetail()
        self.ordernumber = self.page_get_ordernumber()
        print("购买商品的订单号为：", self.ordernumber)