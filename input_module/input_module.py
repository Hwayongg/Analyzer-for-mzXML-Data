# -*- coding: utf-8 -*-
# Made by HY.Jang
# input_module.py >> .mzXMLÆÄÀÏÀ» ÆÄÀÌ½ã¿¡ ·ÎµåÇØÁÜ
'''
from pyopenms import ~ (.mzXML)
'''

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from library.pyOpenMS.pyopenms import *


'''
import ..library.pyopenms


pyopenms.__version__
# 2. pyopenms¸¦ ÀÌ¿ë, mzXMLÆÄÀÏÀ» ÆÄÀÌ½ã¿¡ ·Îµå
class file_loader:
    file_path = ''
    def __init__(self):
        print("")
    def input_path(self):
        self.file_path = input("")
        if self.file_path == 'sample':
            self.file_path = 'G:\Python\sample\sample.mzXML'
        print("" %self.file_path)
    def file_open(self):
        print(" >>> Complete!\n\n")




'''


'''
if __name__=="__main__":
    file_path = 'H:\Python\sample.mzXML'
    print('''##### sample의 file path를 입력 #####
##### path: %s #####''' %file_path)'''