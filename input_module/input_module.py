# -*- coding: euc-kr -*-
# Made by HY.Jang
# input_module.py >> .mzXML파일을 파이썬에 로드해줌
'''
from pyopenms import ~ (.mzXML 확장자를 열 게 해주는 패키지)
'''

# 2. pyopenms를 이용, mzXML파일을 파이썬에 로드
class file_loader:
    file_path = ''
    def __init__(self):
        print("┏ 2. 프로그램에 질량분석 데이터 불러오기")
    def input_path(self):
        self.file_path = input("┃ >>> mzXML파일의 경로를 입력해주세요: ")
        if self.file_path == 'sample':
            self.file_path = 'G:\Python\sample\sample.mzXML'
        print("┃ >>> 입력된 경로는 [%s] 입니다." %self.file_path)
    def file_open(self):
        print("┗ >>> Complete!\n\n")

# 파일 패스를 잘못 입력했을 경우에 다시 입력하도록 하는 코드를 넣어보면 어떨까?






if __name__=="__main__":
    file_path = 'G:\Python\sample\sample.mzXML'
    print('''##### file_path에 예제값 입력 완료! #####
##### path: %s #####''' %file_path) 
