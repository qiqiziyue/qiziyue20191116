class AddGoods(object):
    search_ipt_loc1 = ('name','goods_name')  #搜索框
    search_ipt_loc2 = ('id','cat_name')  #搜索框
    search_ipt_loc3 = ('name','shop_price')  #搜索框
    search_btn_loc = ('id','goods_info_submit')  #搜索框

    def __init__(self,driver):
        self.driver = driver
        self.driver.switch_to.frame('main-frame')
    def input_keyword1(self,text1):
        self.driver.find_element(*self.search_ipt_loc1).send_keys(text1)
    def input_keyword2(self,text2):
        self.driver.find_element(*self.search_ipt_loc2).send_keys(text2)
    def input_keyword3(self,text3):
        self.driver.find_element(*self.search_ipt_loc3).send_keys(text3)
    def click_search_btn(self):
        self.driver.find_element(*self.search_btn_loc).click()
