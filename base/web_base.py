import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from base.base import Base

class WebBase(Base):
    # web页面公共操作
    # tpshop后台：文章管理-新增文章-所属分类选择
    def web_base_click_classify(self, text):
        time.sleep(1)
        # 点击父所属分类框
        loc = By.CSS_SELECTOR, ".form-control"
        select = Select(self.base_find(loc))

        select.select_by_visible_text(text)

    # 判断页面是否包含指定元素
    def web_base_is_exist(self, text):
        # 1. 组装元素配置信息
        loc = By.XPATH, "//*[text()='{}']".format(text)
        # 2. 找元素
        try:
            # 1. 找元素 修改查找时间为3s
            self.base_find(loc, timeout=3)
            # 2. 输出找到信息
            print("找到：{} 元素！".format(loc))
            # 3. 返回True
            return True
        except:
            # 1. 输出未找到信息
            print("没有找到：{} 元素！".format(loc))
            # 2. 返回False
            return False

