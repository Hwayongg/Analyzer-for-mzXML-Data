# -*- coding: euc-kr -*-
# Made by HY.Jang
# process_module.py >> ��ü �����Ϳ��� �ʿ��� �����͸� ����
'''
from pyopenms import ~ (.mzXML Ȯ���ڸ� �м��ϰ� �� �ִ� ��Ű��)
import numpy
'''

# 3. mzXML���Ͽ��� �ʿ��� �������� ���� >> numpy�������� ����
class data_extractor:
    def __init__(self):
        return
    def BPC(self):
        print('''�� 3. Base Peak Chromatogram ������ ����
�� >>> X�� = retention time
�� >>> Y�� = base peak intensity
�� >>> Complete!
��
��''')
    def MS(self):
        print('''�� 3. Mass Spectrum ������ ����
�� >>> X�� = m/z
�� >>> Y�� = intensity
�� >>> Complete!
��
��''')




if __name__ == '__main__':
    data_extractor().BPC()
    data_extractor().MS()
