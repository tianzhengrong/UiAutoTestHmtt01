from page.page_app_article import PageAppArticle
from page.page_app_login import PageAppLogin
from page.page_mp_article import PageMpArticle
from page.page_mp_login import PageMpLogin
from page.page_mp_order import PageMpOrder
from page.page_tp_login import PageTpLogin
from page.page_tpshop_order import PageTpshopOrder


class PageIn:
    def __init__(self, driver):
        self.driver = driver

    # 获取PageTpLogin对象
    def page_get_PageTpLogin(self):
        return PageTpLogin(self.driver)

    # 获取PageMpLogin对象
    def page_get_PageMpLogin(self):
        return PageMpLogin(self.driver)

    # 获取PageMpArticle对象
    def page_get_PageMpArticle(self):
        return PageMpArticle(self.driver)

    # 获取PageTpshopOrder对象
    def page_get_PageTpshopOrder(self):
        return PageTpshopOrder(self.driver)

    # 获取PageMpOrder对象
    def page_get_PageMpOrder(self):
        return PageMpOrder(self.driver)

    # 获取PageAppLogin对象
    def page_get_PageAppLogin(self):
        return PageAppLogin(self.driver)

    # 获取PageAppArticle对象
    def page_get_PageAppArticle(self):
        return PageAppArticle(self.driver)