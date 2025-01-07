

import nltk
from nltk.tokenize import word_tokenize
from sklearn.feature_selection import VarianceThreshold
import sys
import os
import Visualize as plot



# Process User Queries
def process_query(query, df):
    tokens = word_tokenize(query.lower())
    column = extract_column_name(tokens, df)
    columns = extract_column_names(tokens, df)
    
    if 'mean' in tokens and column:
        return f"Mean of {column}: {df[column].mean()}"
    elif 'median' in tokens and column:
        return f"Median of {column}: {df[column].median()}"
    elif 'mode' in tokens and column:
        return f"Mode of {column}: {df[column].mode()}"
    
    elif 'std' in tokens or 'standard deviation' in tokens and column:
        return f"Standard Deviation of {column}: {df[column].std()}"
    elif 'correlation' in tokens and columns:
        corr_value = df[columns[0]].corr(df[columns[1]])
        return f"Correlation between {columns[0]} and {columns[1]}: {corr_value}"
    elif 'visualization' in tokens or 'plot' in tokens:
        return plot.select_chart_type(tokens, df)  # Ensure this line calls the correct function
    elif 'selectfeatures' in tokens or 'quantitative analysis' in tokens:
        return feature_selection(df)
    else:
        return "Sorry, I couldn't understand the query."

# Extract column names
def extract_column_name(tokens, df):
    for token in tokens:
        if token in df.columns.str.lower():
            return df.columns[df.columns.str.lower() == token][0]
    return None

def extract_column_names(tokens, df):
    columns = [df.columns[df.columns.str.lower() == token][0] for token in tokens if token in df.columns.str.lower()]
    return columns if len(columns) == 2 else None

# Feature Selection
def feature_selection(df):
    selector = VarianceThreshold(threshold=0.1)
    selected_data = selector.fit_transform(df.select_dtypes(include=[float, int]))
    selected_columns = df.columns[selector.get_support(indices=True)]
    return f"Selected features: {selected_columns}"

