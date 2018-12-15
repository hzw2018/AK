#导包
import os

import yaml
#打开yaml文件
class BaseReadLongin():
    def __init__(self,filename):
        self.filename=os.getcwd()+os.sep+"data"+os.sep+filename
    def base_read_long(self):
        #使用pytest,配置文件(会自动获取每个文件的当前路径)运行,路径是当前路径
        with open(self.filename,"r",encoding="utf-8") as f:
            return yaml.load(f)




if __name__ == '__main__':
    a = BaseReadLongin("data_longin.yaml")
    print(a.filename)
