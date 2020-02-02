from heapq import nlargest
import argparse
import os
import sys

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

def pdf_wfreq(url, wf=100):
    txt_file = 'text2analyse'
    cmd1 = 'wget ' + "\"" + url + "\""  + ' -O ' + (txt_file + '.pdf')    
    cmd2 = 'pdftotext -enc UTF-8 ' + txt_file + '.pdf'  + ' ' + txt_file + '.txt' &> /dev/null
    
    os.system(cmd1)
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
        for i in most_freq:
            print(i + ':', word_dict[i])
        


        


