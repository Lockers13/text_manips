from heapq import nlargest
import argparse
import os
import sys

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

def pdf_wfreq(path, wf=100):
    """Takes a specified pdf and converts it to .txt format

    Subsequently analyses the frequency of words occurring in the said .txt file and returns result in a dictionary
    Number of words returned is given by keyword argument wf"""

    isUrl = path.startswith('http')
    txt_file = 'text2analyse'
    if isUrl:
        cmd1 = 'wget ' + "\"" + path + "\""  + ' -O ' + (txt_file + '.pdf >/dev/null 2>&1')
        os.system(cmd1)
        path = txt_file+'.pdf'
 
    cmd2 = 'pdftotext -enc UTF-8 ' + "\"" + path + "\"" + ' ' + "\"" + txt_file + '.txt\"'  
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
        print('{0} : {1}'.format(i, word_dict[i]))     



#    with open('word_freq.txt', 'w+') as f:
#        for i in most_freq:
#            f.write('{0} : {1}\n'.format(i, word_dict[i]))
        
