class ShangzhiyiPage(object):
    def __init__(self,driver):
        self.driver = driver
    #页面元素 'name','class_name'八种定位元素
    search_ipt_loc1 = ('name','username')  #搜索框
    search_ipt_loc2 = ('name','password')  #搜索框
    search_btn_loc = ('class name','button2')  #搜索按钮
    #对每个元素操作，封装一个方法
    def input_keyword1(self,text1):
        """输入关键字"""
        self.driver.find_element(*self.search_ipt_loc1).send_keys(text1)
    def input_keyword2(self,text2):
        """输入关键字"""
        self.driver.find_element(*self.search_ipt_loc2).send_keys(text2)
        #"""点击搜搜按钮"""
    def click_search_btn(self):
        self.driver.find_element(*self.search_btn_loc).click()
    #业务组合
    def search(self,text1,text2):
        self.input_keyword1(text1)
        self.input_keyword2(text2)
        self.click_search_btn()