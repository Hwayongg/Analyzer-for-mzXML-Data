# -*- coding: euc-kr -*-
# Made by HY.Jang
# output.py >> ������ �����͸� �׷����� �׷��ְ� �̹��� ���Ϸ� ����

'''
import matplotlib (�� matplotlib�� �ƴϴ��� �����͸� �÷��� ���ִ� ��Ű��
'''

# 4. �����͸� �׷����� �׸��� �̹��� ���Ϸ� ����
class plot_and_saver():
    def __init__(self):
        return
    def BPC(self):
        # ���⼭ plot�Ҷ� x, y�� �̸��� ���� ����
        print ('''�� 4. BPC �׷��� �׸��� �̹��� ���Ϸ� ����
�� >>> X�� = retention time
�� >>> Y�� = base peak intensity
�� >>> Complete!\n\n''')
    def MS(self):
        print ('''�� 4. MS �׷��� �׸��� �̹��� ���Ϸ� ����
�� >>> X�� = m/z
�� >>> Y�� = intensity
�� >>> Complete!\n\n''')
        



if __name__ == '__main__':
    plot_and_saver().BPC()
    plot_and_saver().MS()
