import pytest
from testcase.web_test.pages.baidu_page import BaiduPage
from testcase.web_test.pages.shangzhiyi_page import ShangzhiyiPage
from testcase.web_test.pages.menu_page import MenuPage
from testcase.web_test.pages.addgoods_page import AddGoods
from testcase.web_test.pages.goodlist_page import GoodlistPage
from datetime import datetime
import os
@pytest.fixture
def selenium(selenium):
    selenium.implicitly_wait(10)
    selenium.maximize_window()
    return selenium

@pytest.fixture
def chrome_options(chrome_options):
    chrome_options.add_argument('--start-maximized')
    # chrome_options.add_argument('--headless')
    return chrome_options
@pytest.fixture
def baidu_page(selenium):
    selenium.get('http://www.baidu.com')
    return BaiduPage(selenium)
@pytest.fixture
def login_page(selenium):
    selenium.get('http://39.104.14.232/ecshop/wwwroot/admin/privilege.php?act=login')
    return ShangzhiyiPage(selenium)

@pytest.fixture
def menu_page(selenium,login_page):
    login_page.login('admin','123456')
    return MenuPage(selenium)

@pytest.fixture
def addgoods_page(selenium,menu_page):
    #1,进入页面
    menu_page.click_menu('商品管理',"添加新商品")
    #2，把页面对象返回给用例
    return AddGoods(selenium)
@pytest.fixture
def goodslist_page(selenium,menu_page):
    menu_page.click_menu('商品管理',"添加新商品")
    return GoodlistPage(selenium)


def pytest_configure(config):
    if config.getoption('htmlpath'):
        now= datetime.now().strftime('%Y%m%d_%H%M%S')
        config.option.htmlpath=os.path.join(config.rootdir,'reports','_report{now}.html')






