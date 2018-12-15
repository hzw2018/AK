#页面分装,一个页面封装一个方法
import page
from base.base import Base


class PageLongin(Base):
    #输入用户名封装
    def page_input_username(self,username):
        self.base_input(page.loc_uesrname,username)

    #输入密码封装
    def page_input_password(self,password):
        self.base_input(page.loc_password,password)

    #点击按钮封装
    def page_click_longin_btn(self):
        self.base_click(page.loc_btn)