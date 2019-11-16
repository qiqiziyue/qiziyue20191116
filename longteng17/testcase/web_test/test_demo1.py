import logging
import pytest

@pytest.mark.skip
def test_baidu(selenium):
    selenium.get('http://www.baidu.com')
    selenium.find_element_by_id('kw').send_keys('少年的你')
    selenium.find_element_by_id('su').click()

@pytest.mark.skip
def test_baidu2(baidu_page):
    baidu_page.search("少年的你")
@pytest.mark.skip
def test_shangzhiyi(login_page):
    login_page.search("admin","123456")
@pytest.mark.skip
def test_menu(selenium,login_page):
    login_page.search("admin","123456")
    return MenuPage(selenium)

@pytest.mark.skip
def test_add_goods(selenium,menu_page):
    menu_page.search("admin","123456")
    test_add_goods("我的风火轮","神物","9999")

def test_logging():
    logging.debug('调试日志')
    logging.info('点击登录')
    logging.warning('警告，数据文件缺失！')
    logging.error('出错了')
    logging.critical('严重出错')
    # assert 0



