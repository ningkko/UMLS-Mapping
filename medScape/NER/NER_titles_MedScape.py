import subprocess
import os
import sys
import shutil
import glob

filepath = '/n/data1/hsph/biostat/celehs/yih798/drug-disease/MedScape/MedScape_texts/'
folders = ['medicine_txts/', 'pediatrics_txts/', 'surgery_txts/']

for folder in folders:
    for file in os.listdir(filepath+folder):
        if file not in os.listdir(filepath + "NER/titles/" + folder):
            print(file)
            # fn1 = open(filepath+folder+file,'r')
            with open('articles/Articles.txt','w') as f1:
                f1.write(file)
            # fn1.close()
            os.system("sh runMiniNERAllInOne.sh")
            shutil.copy('results/NER_output.txt', filepath + "NER/titles/" + folder + file)
        # shutil.rmtree('results')
        # os.mkdir('results')