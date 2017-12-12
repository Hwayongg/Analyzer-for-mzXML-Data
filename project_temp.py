# -*- coding: utf-8 -*-

import pyopenms
import matplotlib.pyplot as plt

exp = pyopenms.MSExperiment()
pyopenms.FileHandler().loadExperiment('E:\Python\sample.mzXML', exp)


#MS scan number 1 만 load할 수 있도록 하는 parameter
i = 1

#MS를 위한 list 설정
MZ = []
Intensity = []
MassSpectrum = []

#MS 를 위한 tuple 생성
for spectrum in exp:
        for peak in spectrum:
		MZ = peak.getMZ()
		Intensity = peak.getIntensity()
		MassSpectrum = append((MZ, Intensity))
	i += 1

	if i == 2 :
		break

#MS plotting
fig, axes = plt.subplots(figsize = (14,4))
axes.plot(*zip(*MassSpectrum))
axes.set_xlabel("m/z")
axes.set_ylaber("Intensity")

#MS를 위한 list 설정
RetentionTime = []
BasePeakIntensity = []
BasePeakChromatogram = []

#BPC 를 위한 tuple 생성
for spectrum in exp:
	for peak in spectrum:
		RetentionTime = peak.getRT()
		BasePeakIntensity = peak.getBasePeak()
		BasePeakChromatogram = append((RetentionTime, BasePeakIntensity))

#BPC Plotting
fig, axes = plt.subplots(figsize = (14,4))
axes.plot(*zip(*BasePeakChromatogram))
axes.set_xlabel("Retention Time")
axes.set_ylaber("Base Peak Intensity")
