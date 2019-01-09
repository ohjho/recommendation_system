# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 11:34:47 2019

@author: Ray
"""
#%% IMPORT
from sys import path

path.insert(0, '../')

import pandas as pd
from Data_cleaning import get_clean_data

bookFile='../data/BX-Books.csv'
books=pd.read_csv(bookFile,sep=";",header=0,error_bad_lines=False, usecols=[0,1,2],index_col=0,names=['isbn',"title","author"],encoding='ISO-8859-1')

_, _, df_ratings = get_clean_data(path='../data/')
data = df_ratings.copy()
#%% THRESHOLD FILTER
usersPerISBN = data.isbn.value_counts()
ISBNsPerUser = data.user.value_counts()

data = data[data["isbn"].isin(usersPerISBN[usersPerISBN>100].index)]
data = data[data["user"].isin(ISBNsPerUser[ISBNsPerUser>100].index)]
#%% CREATE RATINGS MATRIX
ratings_matrix = data.pivot_table(index = ['user'], columns = ['isbn'], values = 'rating')
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
item = '0385504209'
itemRatings = ratings_matrix[item]

similarItems = ratings_matrix.corrwith(itemRatings).dropna()
similar_df = pd.DataFrame(similarItems)
similar_df = similar_df.sort_values(0, ascending=False).reset_index()
#%% 
def bookMeta(isbn):
  try:
    title = books.at[isbn,"title"]
    author = books.at[isbn,"author"]
    return title, author
  
  except:
    return 'nan', 'nan'
  
similar_df["title"] = similar_df["isbn"].apply(bookMeta)
