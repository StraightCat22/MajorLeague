# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 13:28:04 2022

@author: leesw
"""
import pandas as pd
import numpy as np

data1 = pd.read_excel('성적테이블.xlsx',  header = 0, usecols = [0,4])

data1['이수학점'] = 0

data1.rename(columns = {"취득학점(평균)" : "Credit" }, inplace=True)

data1.head()
data1.info()

#data1 = data1.drop(['학년도', '학기' ,'평점(평균)'], axis=1)

data2 = data1.groupby('ID').sum()


data2.to_csv('이수학점.csv',index = True)


