# -*- coding: euc-kr -*-
# Made by HY.Jang
# process_module.py >> 전체 데이터에서 필요한 데이터를 추출
'''
from pyopenms import ~ (.mzXML 확장자를 분석하게 해 주는 패키지)
import numpy
'''

# 3. mzXML파일에서 필요한 데이터의 추출 >> numpy형식으로 저장
class data_extractor:
    def __init__(self):
        return
    def BPC(self):
        print('''┏ 3. Base Peak Chromatogram 데이터 추출
┃ >>> X축 = retention time
┃ >>> Y축 = base peak intensity
┃ >>> Complete!
┃
┃''')
    def MS(self):
        print('''┏ 3. Mass Spectrum 데이터 추출
┃ >>> X축 = m/z
┃ >>> Y축 = intensity
┃ >>> Complete!
┃
┃''')




if __name__ == '__main__':
    data_extractor().BPC()
    data_extractor().MS()
