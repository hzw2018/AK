import os
import sys

sys.path.append(os.getcwd())
import pytest
from base.base_read_longin import BaseReadLongin
from base.get_driver import get_driver
from page.page_longin import PageLongin

#传入的参数化数据格式是列表里面套元组,所以要将数据转化到这种格式
def get_data():
    arrs = []
    for data in BaseReadLongin("data_longin.yaml").base_read_long().values():
        arrs.append((data.get("username"),data.get("password")))
        return arrs





class TestLongin():
    #实例化页面对象
    def setup_class(self):
        self.longin = PageLongin(get_driver())
        self.longin.driver.start_activity("com.vcooline.aike",".umanager.LoginActivity")

    #关闭driver打开出窗口
    def teardown_class(self):
        self.longin.driver.quit()

    #根据步骤调用页面方法
    @pytest.mark.parametrize("username,password",get_data())
    def testlongin(self,username,password):
        self.longin.page_input_username(username)
        self.longin.page_input_password(password)
        self.longin.page_click_longin_btn()
    def test_11(self):
        print("输出test_11")

