from heapq import nlargest
import argparse
import os
import sys

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

def pdf_wfreq(url, wf=100):
    txt_file = 'text2analyse'
    cmd1 = 'wget ' + "\"" + url + "\""  + ' -O ' + (txt_file + '.pdf >/dev/null 2>&1') 
    cmd3 = 'pdftotext &> /dev/null; if [ $? -ne 0 ]; then echo echo \"It appears that pdftools is not installed...would you like to install it? y/n\" else exit 0 fi read answer if [ $answer == \'y\' ]; then sudo apt-get install poppler-utils else exit 0 fi'
    cmd2 = 'pdftotext -enc UTF-8 ' + txt_file + '.pdf'  + ' ' + txt_file + '.txt'
    
    
    os.system(cmd1)
    os.system(cmd3)
    os.system(cmd2)
    
    with open(txt_file+'.txt', "r") as f:
        word_dict = {}
        words = f.read().split()
        stop_ws = set(stopwords.words('english'))
        for i in words:
            i = i.lower()
            if i not in stop_ws:
                try:
                    i.encode('ascii')
                    if i in word_dict:
                        word_dict[i] += 1
                    else:
                        word_dict[i] = 1
                except UnicodeEncodeError:
                    continue
        
    most_freq = nlargest(wf, word_dict, key=word_dict.get)
    with open('word_freq.txt', 'w+') as f:
        for i in most_freq:
            f.write('{0} : {1}\n'.format(i, word_dict[i]))
        


        

