# -*- coding: euc-kr -*-
# Made by HY.Jang
# output.py >> 추출한 데이터를 그래프로 그려주고 이미지 파일로 저장

'''
import matplotlib (꼭 matplotlib이 아니더라도 데이터를 플로팅 해주는 패키지
'''

# 4. 데이터를 그래프로 그리고 이미지 파일로 저장
class plot_and_saver():
    def __init__(self):
        return
    def BPC(self):
        # 여기서 plot할때 x, y축 이름을 같이 저장
        print ('''┃ 4. BPC 그래프 그리고 이미지 파일로 저장
┃ >>> X축 = retention time
┃ >>> Y축 = base peak intensity
┗ >>> Complete!\n\n''')
    def MS(self):
        print ('''┃ 4. MS 그래프 그리고 이미지 파일로 저장
┃ >>> X축 = m/z
┃ >>> Y축 = intensity
┗ >>> Complete!\n\n''')
        



if __name__ == '__main__':
    plot_and_saver().BPC()
    plot_and_saver().MS()
