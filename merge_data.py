from Data_cleaning import get_clean_data
df_books, df_users, df_ratings = get_clean_data()
import pandas as pd


def merge_data_frame(user_argv=-1, isbn_argv=-1):

    # merge ratings table with users table by user_ID
    df_merges = pd.merge(df_ratings, df_users, on='user')

    # based on the previous df_merges merge with books table by isbn
    df_merges = pd.merge(df_merges, df_books, on='isbn')

    # find user that has more than [No. of review] and filter it
    df_merges['user'] = df_merges.groupby('isbn')['user'].filter(lambda x: len(x) > user_argv)

    # find books that has more than [No. of users] and filter it
    df_merges['isbn'] = df_merges.groupby('user')['isbn'].filter(lambda x: len(x) > isbn_argv)

    # drop out the users that is null
    df_merges = df_merges[pd.notnull(df_merges['user'])]

    # drop out the books that is null
    df_merges = df_merges[pd.notnull(df_merges['isbn'])]

    # convert the user_ID to string type
    df_merges['user'] = df_merges['user'].astype('int').astype('str')

    return df_merges
