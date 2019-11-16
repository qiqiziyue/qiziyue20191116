

class BaiduPage(object):
    def __init__(self,driver):
        self.driver = driver
    #页面元素 'name','class_name'八种定位元素
    search_ipt_loc = ('id','kw')  #搜索框
    search_btn_loc = ('id','su')  #搜索按钮
    #对每个元素操作，封装一个方法
    def input_keyword(self,text):
        """输入关键字"""
        self.driver.find_element(*self.search_ipt_loc).send_keys(text)
        #"""点击搜搜按钮"""
    def click_search_btn(self):
        self.driver.find_element(*self.search_btn_loc).click()
    #业务组合
    def search(self,text):
        self.input_keyword(text)
        self.click_search_btn()

