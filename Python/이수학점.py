# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 13:28:04 2022

@author: leesw
"""
import pandas as pd
import numpy as np

data1 = pd.read_excel('성적테이블.xlsx',  header = 0, usecols = [0,1,4])

idx_nm_22 = data1[data1['학년도']== 2022 ].index

data2 = data1.drop(idx_nm_22)

data3 = data2.groupby('ID').sum()
#data1['이수학점'] = 0

data3 = data3.drop(columns = "학년도" ,  axis=1)

data3.rename(columns = {"취득학점(평균)" : "취득학점(총합)" }, inplace=True)


data3.to_csv('총합이수학점_2022제외.csv',index = True)