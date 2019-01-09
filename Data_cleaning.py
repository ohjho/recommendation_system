import pandas as pd

def convert_year(in_string):
    '''Returns input as integer if possible, else None'''
    try:
        return int(in_string)
    except:
        return None

def get_country(in_string):
    '''Return the country element from the location.'''
    try:
        return in_string.rsplit(',', 1)[1].strip('.;-')
    except:
        return in_string

def get_province(in_string):
    '''Return the province/state/area element from the location'''
    try:
        return in_string.rsplit(',', 2)[1].strip('.;-')
    except:
        return None

def get_clean_data(path='./data/'):
    '''
    Returns 3 cleaned datasets. Enter the path if the csv files is not under
    \data\ in your system
    :return:
    DataFrame - pandas dataframe of books
    DataFrame - pandas dataframe of users
    DataFrame - pandas dataframe of ratings

    '''
    # skip some lines. Only like 5 of them. Errors likely because there
    # are semicolons in the title and pandas recognizes it as another column
    df_books = pd.read_csv(
        path + "BX-Books.csv", sep=';', encoding="ISO-8859-1", error_bad_lines=False
    )
    df_users = pd.read_csv(path + "BX-Users.csv", sep=';', encoding="ISO-8859-1")
    df_ratings = pd.read_csv(
        path + "BX-Book-Ratings.csv", sep=';', encoding="ISO-8859-1"
    )
    df_books.columns = [
        'isbn', 'title', 'author', 'pub_year', 'publisher', 'url_s', 'url_m',
        'url_l'
    ]
    df_ratings.columns = ['user', 'isbn', 'rating']
    df_users.columns = ['user', 'location', 'age']
    df_books.pub_year = (
        df_books.pub_year.apply(convert_year)
    )
    # Drop the 3 bad rows
    df_books = df_books[~df_books.pub_year.isna()]

    # pub_year 0 most certainly means unknown value or null
    # anything > 2018 don't make sense either
    df_books.pub_year[
        (df_books.pub_year > 2018) | (df_books.pub_year == 0)
        ] = None

    # Age 0 doesnt make sense and is most likely unknown or unrecorded value
    # Age > 122 doesnt make sense either as 122 is the recorded oldest person
    # on earth. (Prolly a lot of those over 100 are errors too but we cant
    # tell)
    df_users.age[(df_users.age == 0) | (df_users.age > 122)] = None
    df_users["country"] = df_users.location.apply(get_country)
    df_users["province"] = df_users.location.apply(get_province)
    return df_books, df_users, df_ratings

################################################################################
def get_merged_data_frame(user_argv=-1, isbn_argv=-1, path='./data/'):
    '''
    Returns a merged dataframe of users, books, ratings.
    :param user_argv: integer, threshold to filter users fewer than this number of
        books rated
    :param isbn_argv: integer, threshold to filter books that has fewer than this
        number of ratings.
    :return: dataframe
    '''


    df_books, df_users, df_ratings = get_clean_data(path=path)

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