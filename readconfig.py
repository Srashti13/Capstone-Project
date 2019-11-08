import configparser
import os.path
from os import path
import os
import subprocess

config = configparser.ConfigParser()
config.read('example.ini')

for section_name in config.sections():
	print('Section:', section_name)
	print(' Options:', config.options(section_name))
	for name, value in config.items(section_name):
		print(' {} = {}'.format(name,value))
	print()

inputsone = config.items('TestOne')[2][1]
inputstwo = config.items('TestOne')[3][1]
inputsthree = config.items('TestOne')[4][1]
print(inputstwo)

filetorun = r'D:\capstone local\UMLS\umls_flowchart_1\classifier.py'

print(os.path.exists(filetorun))

os.system('powershell.exe python {}'.format(filetorun))