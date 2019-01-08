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
#%%
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
# filter by both ISBN and users
usersPerISBN = data.isbn.value_counts()
ISBNsPerUser = data.user.value_counts()

data = data[data["isbn"].isin(usersPerISBN[usersPerISBN>10].index)]
data = data[data["user"].isin(ISBNsPerUser[ISBNsPerUser>10].index)]
#%% CREATE RATINGS MATRIX
userItemRatingMatrix=pd.pivot_table(data, values='rating',
                                    index=['user'], columns=['isbn'])
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
import numpy as np
from scipy.spatial.distance import hamming

def distance(user1,user2):
        try:
            user1Ratings = userItemRatingMatrix.transpose()[str(user1)]
            user2Ratings = userItemRatingMatrix.transpose()[str(user2)]
            distance = hamming(user1Ratings,user2Ratings)
        except: 
            distance = np.NaN
        return distance 
#%%
def nearestNeighbors(user,K=10):
    allUsers = pd.DataFrame(userItemRatingMatrix.index)
    allUsers = allUsers[allUsers.user!=user]
    allUsers["distance"] = allUsers["user"].apply(lambda x: distance(user,x))
    KnearestUsers = allUsers.sort_values(["distance"],ascending=True)["user"][:K]
    return KnearestUsers
#%% DEBUGGING
"""NNRatings = userItemRatingMatrix[userItemRatingMatrix.index.isin(KnearestUsers)]
NNRatings"""
"""avgRating = NNRatings.apply(np.nanmean).dropna()
avgRating.head()"""
"""booksAlreadyRead = userItemRatingMatrix.transpose()[str(user)].dropna().index
booksAlreadyRead"""
""""avgRating = avgRating[~avgRating.index.isin(booksAlreadyRead)]"""

#%%
def bookMeta(isbn):
    title = books.at[isbn,"title"]
    author = books.at[isbn,"author"]
    return title, author

def faveBooks(user,N):
    userRatings = data[data["user"]==user]
    sortedRatings = pd.DataFrame.sort_values(userRatings,['rating'],ascending=[0])[:N] 
    sortedRatings["title"] = sortedRatings["isbn"].apply(bookMeta)
    return sortedRatings

def topN(user,N=3):
    KnearestUsers = nearestNeighbors(user)
    NNRatings = userItemRatingMatrix[userItemRatingMatrix.index.isin(KnearestUsers)]
    avgRating = NNRatings.apply(np.nanmean).dropna()
    booksAlreadyRead = userItemRatingMatrix.transpose()[user].dropna().index
    avgRating = avgRating[~avgRating.index.isin(booksAlreadyRead)]
    topNISBNs = avgRating.sort_values(ascending=False).index[:N]
    return pd.Series(topNISBNs).apply(bookMeta)
#%% DEBUGGING
"""N=3
topNISBNs = avgRating.sort_values(ascending=False).index[:N]
pd.Series(topNISBNs).apply(bookMeta)"""
"""user = '204622'
topN(user)"""

