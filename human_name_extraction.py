# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 13:32:20 2017

@author: anjalidharmik
"""

import codecs
import pandas as pd
from nltk.corpus import names

def extract_name_and_gender(file_name):
    list_of_names =[]
    list_of_male_names = names.words('male.txt')
    list_of_female_names =names.words('female.txt')
    list_of_names.extend(list_of_male_names)
    list_of_names.extend(list_of_female_names)

    doc_str = codecs.open(file_name,"r", 'utf-8','ignore').read()
    
    cap_val_list = doc_str.split('\r\n')
    for i in cap_val_list:
        name_l = []
        if ' ' in i:
            val_list = i.split(' ')
            
            for j in val_list:
               j = j.replace(',','')
               if j in list_of_names:
                   if j in list_of_male_names:
                       gender = 'M'
                       
                       name_l.append((j,gender))
                   elif j in list_of_female_names:
                       gender= 'F'
                       
                       name_l.append((j,gender))
                   else:
                       gender= ''
                       name_l.append((j,gender))
                       
            if len(name_l)>1:
                filename = (file_name.split('/')[-1]).split('.pgr')[0]
           
                if  name_l[0][0] == name_l[1][0]:
                    name =''
                else:
                    name = name_l[0][0]+' '+name_l[1][0]    
                    
                gender = name_l[0][1]
                if name != "":
                    df_out = pd.DataFrame({"Filename":[filename],"Name":[name],"Gender":[gender]})
                    print df_out

file_name = '/home/anjalidharmik/tutorial/git/demo.txt'
extract_name_and_gender(file_name)
                 