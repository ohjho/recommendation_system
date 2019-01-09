# recommendation_system
Xccelerate Data Science Bootcamp Collaborative Project: 4 flavours of recommendation systems using the [Booking Crossing Dataset](http://www2.informatik.uni-freiburg.de/~cziegler/BX/) which is also included [here](data/) in this repo.

See the project's details [here](project_details.md)

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
![python versions](https://img.shields.io/badge/python-3.5%20%7C%203.6%20%7C%203.7-blue.svg)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)

## How to Use this repo
1. Clone this repo:
```
$ git clone https://github.com/ohjho/recommendation_system.git
$ cd recommendation_system
```
2. install the requirements. We **highly recommend** doing this inside a [virtualenv][url_virtualenv] and avoid [dependency hell](https://medium.com/knerd/the-nine-circles-of-python-dependency-hell-481d53e3e025).  
```
#---------------- optional ------------------
$ mkvirtualenv --python=`which python3` NameOfYourEnv
$ workon NameOfYourEnv
#--------------------------------------------

(NameOfYourEnv) $ pip install -r requirements.txt
```
and just check and resolve any packages dependency issues if they show up under `pip check`. It should say `No broken requirements found.`  

3. Start Jupyter notebook
```
$ jupyter notebook
```

## Data Cleaning
#### How to use data_cleaning.py
The script data_cleaning.py will import the datasets and clean the data.

To get 3 separate dataframes, do this
```
from data_cleaning import get_clean_data
df_books, df_users, df_ratings = get_clean_data()
```
And if the csv files are not under `data/`, use the path argument.

To get one merged dataframe, do this:
```
from data_cleaning import get_merged_data_frame
df_merged = get_merged_data_frame(user_argv=user_threshold, isbn_argv=book_threshold)
```
where user_threshold is the threshold to filter out users with fewer than this number of books rated.
books_threshold is the books counterpart
And if the csv files are not under "/data/", use the path argument.


## Modeling
### [A. Content-based Filtering](content_based_filtering/)
### [B. Collaborative Filtering](collaborative_filtering/)
### [C. Latent Factor Analysis](latent_factor_analysis/)

[url_virtualenv]: https://virtualenvwrapper.readthedocs.io/en/latest/
