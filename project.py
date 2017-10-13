# project.py

# 1. 필요한 모듈, 패키지, 라이브러리 등을 import
import input_module.input_module
import process_module.process_module
import output_module.output_module
print('''┏ 1. import
┗ >>> Complete!\n\n''')



# 2. 파일 로드
file_loader = input_module.input_module.file_loader()
file_loader.input_path()
file_loader.file_open()



# 3 & 4. 데이터 추출(process_module) 후 그래프로 그리고 이미지 파일로 저장(output_module)
# Base Peak Chromatogram
BPC_extractor = process_module.process_module.data_extractor()
BPC_plot_and_saver = output_module.output_module.plot_and_saver()
BPC_extractor.BPC()
BPC_plot_and_saver.BPC()
# Mass Spectrum
MS_extractor = process_module.process_module.data_extractor()
MS_plot_and_saver = output_module.output_module.plot_and_saver()
MS_extractor.MS()
MS_plot_and_saver.MS()

# cmd창에서 실행시 '엔터'를 입력하기 전까지 대기하는 코드
input('')
