import os

import yaml
class BaseYaml():
    def __init__(self,filename):
        self.filename = os.getcwd()+os.sep+"data"+os.sep+filename
    def base_yaml(self):
        #打开文件流
        with open("../data/data_longin.yaml","r",encoding="utf-8") as f:
            #读取文件
            return yaml.load(f)