import pytest

import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.read_yaml import read_yaml


class TestMpArticle:
    # 1.初始化
    def setup_class(self):
        # 1.获取driver
        driver = GetDriver.get_web_driver(page.url_houtai)
        # 2.获取统一入口类
        self.page_in = PageIn(driver)
        # 3.获取PageMpLogin对象并调用成功登录依赖方法
        self.page_in.page_get_PageMpLogin().page_mp_login(username="admin", password="123456", code="8888")
        # 4.获取PageMpArticle页面对象
        self.article = self.page_in.page_get_PageMpArticle()

    # 2.结束
    def teardown_class(self):
        # 关闭driver
        GetDriver.quit_web_driver()

    # 3.测试发布文章方法
    @pytest.mark.parametrize("title,content", read_yaml("mp_article.yaml"))
    def test_mp_article(self, title, content):
        # 调用发布文章业务方法
        self.article.page_mp_article(title, content)
        # 查看断言信息
        print("已发布文章的标题为：", self.article.page_get_info())