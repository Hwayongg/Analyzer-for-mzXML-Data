# -*- coding: euc-kr -*-
# Made by HY.Jang
# input_module.py >> .mzXMLÆÄÀÏÀ» ÆÄÀÌ½ã¿¡ ·ÎµåÇØÁÜ
'''
from pyopenms import ~ (.mzXML È®ÀåÀÚ¸¦ ¿­ °Ô ÇØÁÖ´Â ÆÐÅ°Áö)
'''

# 2. pyopenms¸¦ ÀÌ¿ë, mzXMLÆÄÀÏÀ» ÆÄÀÌ½ã¿¡ ·Îµå
class file_loader:
    file_path = ''
    def __init__(self):
        print("¦® 2. ÇÁ·Î±×·¥¿¡ Áú·®ºÐ¼® µ¥ÀÌÅÍ ºÒ·¯¿À±â")
    def input_path(self):
        self.file_path = input("¦­ >>> mzXMLÆÄÀÏÀÇ °æ·Î¸¦ ÀÔ·ÂÇØÁÖ¼¼¿ä: ")
        if self.file_path == 'sample':
            self.file_path = 'G:\Python\sample\sample.mzXML'
        print("¦­ >>> ÀÔ·ÂµÈ °æ·Î´Â [%s] ÀÔ´Ï´Ù." %self.file_path)
    def file_open(self):
        print("¦± >>> Complete!\n\n")

# ÆÄÀÏ ÆÐ½º¸¦ Àß¸ø ÀÔ·ÂÇßÀ» °æ¿ì¿¡ ´Ù½Ã ÀÔ·ÂÇÏµµ·Ï ÇÏ´Â ÄÚµå¸¦ ³Ö¾îº¸¸é ¾î¶³±î?






if __name__=="__main__":
    file_path = 'H:\Python\sample.mzXML'
    print('''##### sample의 file path를 입력 #####
##### path: %s #####''' %file_path)