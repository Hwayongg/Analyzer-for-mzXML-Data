# project.py

# Step1. 필요한 모듈, 패키지, 라이브러리 등을 import
'''
import mzXML_analyzer
import numpy 등...
그 외의 코딩한 모듈들도 호출
'''
import input.input
import process.process
import output.output
print("Step1. import 완료!")

# Step2. 파일 로드 함수 실행
input.input.file_open()

# Step3. 데이터 추출 함수 실행
process.process.BPC_data_extractor()
process.process.MS_data_extractor()

# Step4. 데이터를 함수로 그리고 이미지 파일로 저장하는 함수 실행
output.output.plot_and_save_BPC()
output.output.plot_and_save_MS()
