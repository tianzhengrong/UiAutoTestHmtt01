from selenium.webdriver.common.by import By

# tpshop前端登录页面url
url_mp = "http://127.0.0.1/Home/user/login.html"
# tpshop后台管理url
url_houtai = "http://localhost/Admin/Admin/login"


"""以下数据为tpshop前端登录模块配置数据"""
# 用户名
tp_username = (By.CSS_SELECTOR, "[name='username']")
# 密码
tp_passward = (By.CSS_SELECTOR, "[name='password']")
# 验证码
tp_code = (By.CSS_SELECTOR, "[name='verify_code']")
# 登录按钮
tp_login_btn = (By.CSS_SELECTOR, ".J-login-submit")
# 昵称
tp_nickname = (By.CSS_SELECTOR, ".red.userinfo")

"""以下数据为tpshop后台登录模块配置数据"""
# 用户名
mp_username = (By.CSS_SELECTOR, "[name='username']")
# 密码
mp_passward = (By.CSS_SELECTOR, "[name='password']")
# 验证码
mp_code = (By.CSS_SELECTOR, "[name='vertify']")
# 登录按钮
mp_login_btn = (By.CSS_SELECTOR, "[name='submit']")
# 昵称
mp_nickname = (By.XPATH, "//dt[text()='admin']")

"""以下数据为tpshop后台添加文章模块配置数据"""
# 系统 按钮
mp_system = By.XPATH, "//a[text()='系统']"
# 文章
mp_article = By.CSS_SELECTOR, ".ico-system-3"
# iframe1（点击新增文章前需要切换表单）
mp_iframe1 = By.CSS_SELECTOR, "#workspace"
# 新增文章
mp_add_article = By.XPATH, "//span[text()='新增文章']"
# 标题
mp_title = By.CSS_SELECTOR, ".input-txt"
# 显示
mp_show = By.CSS_SELECTOR, ".cb-enable"
# iframe2（输入文章内容时需要切换表单）
mp_iframe2 = By.CSS_SELECTOR, "#ueditor_0"
# 文章内容
mp_content = By.CSS_SELECTOR, "body[class='view']"
# 确认提交
mp_submit = By.CSS_SELECTOR, ".ncap-btn-big"
# 结果验证 （文章列表中首篇文章的标题）
mp_first_title = By.CSS_SELECTOR, "#flexigrid > table > tbody > tr:nth-child(1) > td:nth-child(2) > div"

"""以下为tpshop后台 订单模块配置数据"""
# 清除缓存
mp_clearcache = By.XPATH, "//a[contains(text(),'清除缓存')]"
# 待处理订单(需要切换到iframe1表单)
mp_order = By.CSS_SELECTOR, ".ice_w"
# 订单编号
mp_ordernumber = By.CSS_SELECTOR, r"#\31 527 > td:nth-child(2) > div"

"""以下为tpshop购买前端购买商品配置数据"""
# tpshop 首页按钮
tpshop_homepage = By.XPATH, "//*[text()='首页']"
# tpshop 搜索框
tpshop_search = By.CSS_SELECTOR, ".ecsc-search-input"
# tpshop 搜索按钮
tpshop_search_btn = By.CSS_SELECTOR, ".ecsc-search-button"
# tpshop 加入购物车
tpshop_addshopcar = By.CSS_SELECTOR, ".p-btn"  # 默认点击第一个商品的 加入购物车按钮
# tpshop 立即购买 按钮
tpshop_buy = By.CSS_SELECTOR, "#join_cart_now"
# tpshop 提交订单
tpshop_submitorder = By.CSS_SELECTOR, ".Sub-orders"
"""查看订单号 方法"""
# tpshop 订单详情
tpshop_orderdetail = By.XPATH, "//*[text()='订单详情']"
# # tpshop 获取订单号
tpshop_ordernumber = By.CSS_SELECTOR, "span>b"

"""以下为今日头条app元素配置信息"""
# 今日头条包名
appPackage = "com.ss.android.article.news"
# 今日头条启动名
appActivity = ".activity.MainActivity"
# 底部 未登录
app_nologin = By.XPATH, "//*[@index='3' and @class='android.widget.RelativeLayout']"
# 红色登录按钮
app_redlogin = By.ID, "com.ss.android.article.news:id/c04"
# 密码登录
app_codelogin = By.ID, "com.ss.android.article.news:id/bhu"
# 手机号
app_phone = By.ID, "com.ss.android.article.news:id/bhh"
# 密码
app_code = By.ID, "com.ss.android.article.news:id/bhp"
# 登录箭头
app_login_btn = By.ID, "com.ss.android.article.news:id/qa"
# 申请认证（登录成功界面元素）
app_request = By.ID, "com.ss.android.article.news:id/bzp"
# 底部 首页
app_homepage = By.ID, "com.ss.android.article.news:id/ctb"
# 频道区域
app_channel_area = By.ID, "com.ss.android.article.news:id/ad9"
# 文章区域
app_article_area = By.ID, "com.ss.android.article.news:id/a8s"




