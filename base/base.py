from selenium.webdriver.support.wait import WebDriverWait


class Base():
    #初始化driver
    def __init__(self,driver):
        self.driver=driver

    #封装,查找元素 方法
    def base_find_element(self,loc,timeout=30,poll=0.5):
        return WebDriverWait(self.driver,timeout,poll_frequency=poll).until(lambda x:x.find_element(*loc))

    #输入方法的分装
    def base_input(self,loc,value):
        #找元素
        ele = self.base_find_element(loc)
        #清空内容
        ele.clear()
        #输入值
        ele.send_keys(value)

    #点击方法分装
    def base_click(self,loc):
        #获取元素并点击
        self.base_find_element(loc).click()

