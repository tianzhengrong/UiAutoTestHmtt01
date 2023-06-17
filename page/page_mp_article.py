from time import sleep
import page
from base.web_base import WebBase

class PageMpArticle(WebBase):
    # 点击 系统
    def page_click_system(self):
        sleep(1)
        self.base_click(page.mp_system)

    # 点击 文章
    def page_click_article(self):
        sleep(0.5)
        self.base_click(page.mp_article)

    # 点击 新增文章
    def page_click_add_article(self):
        sleep(0.5)
        # 1.切换iframe1
        iframe1 = self.base_find(page.mp_iframe1)
        self.driver.switch_to.frame(iframe1)
        # 2.点击新增文章
        self.base_click(page.mp_add_article)

    # 输入 标题
    def page_input_title(self, title):
        sleep(0.5)
        self.base_input(page.mp_title, title)

    # 选择 分类
    def page_click_classify(self):
        sleep(0.5)
        # 调用WebBase封装方法
        self.web_base_click_classify(text="购物指南")

    # 选择 显示
    def page_click_show(self):
        sleep(0.5)
        self.base_click(page.mp_show)

    # 输入 文章内容
    def page_input_content(self, content):
        sleep(0.5)
        # 1.切换iframe2
        iframe3 = self.base_find(page.mp_iframe2)
        self.driver.switch_to.frame(iframe3)
        # 2.输入内容
        self.base_input(page.mp_content, content)
        # 3.回到默认目录
        self.driver.switch_to.default_content()

    # 点击 确认提交按钮
    def page_click_submit(self):
        sleep(1)
        # 1.切换iframe1
        iframe1 = self.base_find(page.mp_iframe1)
        self.driver.switch_to.frame(iframe1)
        # 2.点击 确认提交按钮
        self.base_click(page.mp_submit)

    # 验证是否提交成功（获取文章列表首行的标题）
    def page_get_info(self):
        return self.base_get_text(page.mp_first_title)

    # 组合发布文章业务方法
    def page_mp_article(self, title, content):
        self.page_click_system()
        self.page_click_article()
        self.page_click_add_article()
        self.page_input_title(title)
        self.page_click_classify()
        self.page_click_show()
        self.page_input_content(content)
        self.page_click_submit()
