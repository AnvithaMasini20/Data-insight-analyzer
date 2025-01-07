#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

# Load Data
def load_data(file_path):
    if file_path.endswith('.csv'):
        return pd.read_csv(file_path)
    elif file_path.endswith('.xlsx'):
        return pd.read_excel(file_path)
    elif file_path.endswith('.json'):
        return pd.read_json(file_path)
    else:
        raise ValueError("Unsupported file type. Please use CSV, Excel, or Json.")

# Clean Data
def clean_data(df):
    df.drop_duplicates(inplace=True)
    df.fillna(df.mean(), inplace=True)
    print("Data cleaned!")
    return df

