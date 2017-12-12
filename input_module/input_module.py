# -*- coding: utf-8 -*-
# Made by HY.Jang
# input_module.py


# 1. import하기
from pyopenms import ~ (.mzXML)

# 2. pyopenms를 이용한 샘플파일로드
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





if __name__=="__main__":
    file_path = 'H:\Python\sample.mzXML'
    print('''##### sample의 file path를 입력 #####
##### path: %s #####''' %file_path''')
