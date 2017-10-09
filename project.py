# ***** 1. 라이브러리 로드 *****
# import mzXML_analyzer
# import numpy 등...
print("Step1. 라이브러리 import 완료! - [mzXML_analyzer / numpy / ... ]\n")

# ***** 2. mzXML_analyzer를 이용, example.mzXML을 파이썬에 로드 *****
print("Step2. 프로그램에 질량분석 데이터 불러오기 완료! - [example.mzXML]\n")

# ***** 3-1. Base Peak Chromatogram을 위한 데이터 추출 *****
# mzXML_analyzer함수를 이용해 데이터를 추출, numpy에 저장
def BPC_data_extractor() :
    print('''Step3-1. Base Peak Chromatogram을 위한 데이터 추출 완료!
        X축 = retention time
        Y축 = base peak intensity''')

# ***** 3-2. Mass Spectrum 을 위한 데이터 추출 *****
# mzXML_analyzer함수를 이용해 데이터를 추출, numpy형식으로 저장
def MS_data_extractor() :
    print('''Step3-2. Mass Spectrum을 위한 데이터 추출 완료!
        X축 = m/z
        Y축 = intensity\n''')

# ***** 4-1. Base Peak Chromatogram plotting *****
# matplotlib 등의 함수를 이용해 그래프를 출력
def plot_BPC() :
    print('''Step4-1. Base Peak Chromatogram 플로팅 완료!''')


# ***** 4-2. Mass Spectrum plotting *****
# matplotlib 등의 함수를 이용해 그래프를 출력
def plot_MS() :
    print('''Step4-2. Mass Spectrum 플로팅 완료!\n''')


# ***** 5. 두 그래프를 각각의 pdf등으로 저장 *****
def plot_saver() :
    print('''Step5. 두 그래프를 각각의 이미지파일로 저장 완료!''')

# ***** 저장된 함수들을 호출 *****
BPC_data_extractor()
MS_data_extractor()

plot_BPC()
plot_MS()

plot_saver()
