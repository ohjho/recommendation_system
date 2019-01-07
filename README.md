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

The script merge_data.py will do again the data_cleaning.py. You can input or not input the argv for the merge_data_frame function.

The user_argv and isbn_argv default is -1, means do not do any filtering.

Here is the demo code to use:
```
from merge_data import merge_data_frame
df = merge_data_frame()

OR

df = merge_data_frame(10,10)
```

