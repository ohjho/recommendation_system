# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 11:34:47 2019

@author: Ray
"""
#%% IMPORT
import pandas as pd
from Data_cleaning import get_clean_data
from merge_data import merge_data_frame

bookFile='../data/BX-Books.csv'
books=pd.read_csv(bookFile,sep=";",header=0,error_bad_lines=False, usecols=[0,1,2],index_col=0,names=['isbn',"title","author"],encoding='ISO-8859-1')

df_books, df_users, df_ratings = get_clean_data(path='../data/')
df_merges = merge_data_frame()
data = df_merges.copy()
data = data.drop(['location',
              'age',
              'country',
              'province',
              'title',
              'author',
              'pub_year',
              'publisher',
              'url_s',
              'url_m',
              'url_l'], axis=1)

#%% RATINGS THRESHOLD FILTERS


#%% CREATE RATINGS MATRIX


#%% THRESHOLD CI
"""from scipy.stats import sem, t
from scipy import mean
confidence = 0.95
data = ratings_per_isbn['count']

n = len(data)
m = mean(data)
std_err = sem(data)
h = std_err * t.ppf((1 + confidence) / 2, n - 1)

start = m - h
print (start)"""
#%% VIS ISBN & USER COUNT
"""import seaborn as sns
ax = sns.distplot(ratings_per_isbn['count'])
ax2 = ax.twinx()
sns.boxplot(x=ratings_per_isbn['count'], ax=ax2)
ax2.set(ylim=(-0.5, 10))"""

#%%

