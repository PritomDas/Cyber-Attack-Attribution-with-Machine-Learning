# -*- coding: utf-8 -*-
"""Preprocessing.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kweHVHfWrhxw2V7DhC26hJ_QspylM5zE

## Importing necessary libraries
"""

import pandas as pd
import numpy as np

#creating a dataframe to read the dataset after mounting in google drive
raw_csv_data = pd.read_csv("extracted_attributes-consolidated.csv")

raw_csv_data.info()

#eye balling the data
raw_csv_data.head(3)

"""## Formatting "Library" column"""

raw_csv_data['Library'] =raw_csv_data['Library'].astype(str).str.replace("[","").str.replace("]","")
raw_csv_data['Library']=raw_csv_data['Library'].str.replace('\s*,\s*',',')

raw_csv_data['Library'] = raw_csv_data['Library'].str.upper()

raw_csv_data.head(3)

"""Creating dummy variable for "Library""""

#copying the old dataframe with a new dataframe meanwhile to mess around
df = raw_csv_data.copy()
encoded_library=df['Library'].str.get_dummies(sep=',')
df=pd.concat([df,encoded_library], axis=1)
pd.options.display.max_columns = None
pd.options.display.max_rows = None
display(df.head(10))

"""# **Observation 1:**

Created new columns with unique libraries and passing boolean representation if a library call was done for a particular resource

## Formatting "Language" column
"""

df['Language'] = df['Language'].astype(str).str.replace("[","").str.replace("]","")
df['Language'] = df['Language'].str.replace('\s*,\s*',',')

df['Language'] = df['Language'].str.upper()

df.head(3)

"""Creating dummy variable for "Language""""

#copying the old dataframe with a new dataframe meanwhile to mess around
df2 = df.copy()
encoded_library2=df2['Language'].str.get_dummies(sep=',')
df2=pd.concat([df2,encoded_library2], axis=1)
pd.options.display.max_columns = None
pd.options.display.max_rows = None
display(df2.head(10))

"""# **Observation 2:**

Created new columns with unique languages and passing boolean representation if a certain language was used for a particular resource

## Unique Library calls made and Langauage used
"""

#unique APT groups in the dataset
pd.unique(df2['APT Group'])

len(df2['APT Group'].unique())

#unique entry points in the dataset
pd.unique(df2['Entry Point'])

len(df2['Entry Point'].unique())

df2.head()

"""# **Oberservation 3:**

Using previous notebooks for unique count observations:

*   There are 12 different APT groups
*   There are 1484 different entry points
*   There are 157 different library calls
*   There are 2184 different resources
*   There are 31 different languages used

# **Exporting the last generated dataframe into a csv file for a new preprocessed dataset**

With Index
"""

preprocessed_data = df2.copy()

preprocessed_data.head(3)

preprocessed_data.to_csv('preprocessed_data.csv', index=True)

# Commented out IPython magic to ensure Python compatibility.
# %ls

#checking with shell command if there was a proper write in the new file created
! cat preprocessed_data.csv

"""# **Exporting the last generated dataframe into a csv file for a new preprocessed dataset**

Without Index
"""

preprocessed_data2 = df2.copy()

preprocessed_data2.head(3)

preprocessed_data2.to_csv('preprocessed_data_without_index.csv', index=False)

# Commented out IPython magic to ensure Python compatibility.
# %ls

#checking with shell command if there was a proper write in the new file created
! cat preprocessed_data_without_index.csv

