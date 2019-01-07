# recommendation_system
Xccelerate Data Science Bootcamp Collaborative Project: 4 flavours of recommendation systems

See the project's details [here](project_details.md)

The script data_cleaning.py will import the datasets and clean the data.
Do this
```
from data_cleaning import get_clean_data
df_books, df_users, df_ratings = get_clean_data()
```

And if the csv files are not under "/data/", use the path argument.
