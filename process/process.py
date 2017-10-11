# process.py >> 전체 데이터에서 필요한 데이터를 추출
'''
from mzXML_analyzer import ~ (.mzXML 확장자를 분석하게 해 주는 패키지)
import numpy
'''

# Step3-1. Base Peak Chromatogram을 위한 데이터 추출
'''mzXML_analyzer함수를 이용해 데이터를 추출, numpy에 저장'''
def BPC_data_extractor() :
    print('''Step3-1. Base Peak Chromatogram을 위한 데이터 추출 완료!
        X축 = retention time
        Y축 = base peak intensity''')

# >>>>> Step3-2. Mass Spectrum 을 위한 데이터 추출
'''mzXML_analyzer함수를 이용해 데이터를 추출, numpy형식으로 저장'''
def MS_data_extractor() :
    print('''Step3-2. Mass Spectrum을 위한 데이터 추출 완료!
        X축 = m/z
        Y축 = intensity\n''')
