# -*- coding: euc-kr -*-
# Made by HY.Jang
# input_module.py >> .mzXML������ ���̽㿡 �ε�����
'''
from pyopenms import ~ (.mzXML Ȯ���ڸ� �� �� ���ִ� ��Ű��)
'''

# 2. pyopenms�� �̿�, mzXML������ ���̽㿡 �ε�
class file_loader:
    file_path = ''
    def __init__(self):
        print("�� 2. ���α׷��� �����м� ������ �ҷ�����")
    def input_path(self):
        self.file_path = input("�� >>> mzXML������ ��θ� �Է����ּ���: ")
        if self.file_path == 'sample':
            self.file_path = 'G:\Python\sample\sample.mzXML'
        print("�� >>> �Էµ� ��δ� [%s] �Դϴ�." %self.file_path)
    def file_open(self):
        print("�� >>> Complete!\n\n")

# ���� �н��� �߸� �Է����� ��쿡 �ٽ� �Է��ϵ��� �ϴ� �ڵ带 �־�� ���?






if __name__=="__main__":
    file_path = 'G:\Python\sample\sample.mzXML'
    print('''##### file_path�� ������ �Է� �Ϸ�! #####
##### path: %s #####''' %file_path) 
