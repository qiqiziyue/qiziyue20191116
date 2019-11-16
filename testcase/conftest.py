import os
from datetime import datetime
def pytest_configure(config):
    if config.getoption('htmlpath'):
        now= datetime.now().strftime("%Y%m%d_%H%M%S")
        config.option.htmlpath=os.path.join(config.rootdir,'reports','report%s.html' % now)

def pytest_addoption(parser):
    parser.addoption("--send-email", action="store_true", help="send email with test report")

def pytest_terminal_summary(config):
    if config.getoption('--send-email'):
        htmlpath = config.getoption('htmlpath')
        Notice().email("正文","主题",[],)




