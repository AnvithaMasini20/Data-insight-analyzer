import pandas as pd
import numpy as np
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.preprocessing import LabelEncoder

class DataInsightAnalyser:
    def __init__(self, data_source):
        self.data_source = data_source
        self.data = self.load_data()

    def load_data(self):
        if self.data_source.endswith('.csv'):
            return pd.read_csv(self.data_source)
        elif self.data_source.endswith('.xlsx'):
            return pd.read_excel(self.data_source)
        elif self.data_source.endswith('.json'):
            return pd.read_json(self.data_source)
        else:
            raise ValueError("Unsupported file format")

    def process_query(self, query):
        tokens = word_tokenize(query)
        tokens = [t for t in tokens if t not in stopwords.words('english')]
        query_type = tokens[0]

        if query_type == 'retrieve':
            column_name = tokens[1]
            return self.data[column_name]
        elif query_type == 'show':
            num_results = int(tokens[1])
            column_name = tokens[3]
            return self.data.nlargest(num_results, column_name)
        elif query_type == 'calculate':
            calculation_type = tokens[1]
            column_name = tokens[2]
            if calculation_type == 'mean':
                return self.data[column_name].mean()
            elif calculation_type == 'median':
                return self.data[column_name].median()
            elif calculation_type == 'standard':
                return self.data[column_name].std()
            elif calculation_type == 'correlation':
                return self.data.corr()[column_name]
        elif query_type == 'clean':
            self.data = self.data.dropna()
            self.data = self.data.drop_duplicates()
            self.data = self.data.apply(LabelEncoder().fit_transform)
            return "Data cleaned successfully"
        else:
            raise ValueError("Unsupported query type")
        if query_type == 'select':
            column_names = tokens[1:]
            rows = tokens[-1]
            if rows == 'all':
                selected_data = self.data[column_names]
            else:
                start, end = map(int, rows.split(':'))
                selected_data = self.data[column_names].iloc[start:end]
            file_format = tokens[-2]
            file_name = tokens[-3]
            if file_format == 'csv':
                selected_data.to_csv(file_name + '.csv', index=False)
            elif file_format == 'excel':
                selected_data.to_excel(file_name + '.xlsx', index=False)
            elif file_format == 'json':
                selected_data.to_json(file_name + '.json', orient='records')
            return "File saved successfully"
        else:
            raise ValueError("Unsupported query type")
        if query_type == 'describe':
            return self.data.describe()
        elif query_type == 'isnotnull':
            column_name = tokens[1]
            return self.data[column_name].notnull().sum()
        elif query_type == 'isnull':
            column_name = tokens[1]
            return self.data[column_name].isnull().sum()
        elif query_type == 'head':
            num_rows = int(tokens[1])
            return self.data.head(num_rows)
        elif query_type == 'tail':
            num_rows = int(tokens[1])
            return self.data.tail(num_rows)
        elif query_type == 'select':
            column_names = tokens[1:]
            return self.data[column_names]
        else:
            raise ValueError("Unsupported query type")
        # Main Program
if _name_ == "_main_":
    # Load data
    file_path = input("Enter the file path of your dataset: ")
    df = load_data(file_path)
    
    # Clean the data
    df = clean_data(df)
    
    # Preview the data
    print("Data Loaded Successfully! Here's a preview:")
    print(df.head())

    # Interactive Query Loop
    while True:
        query = input("\nAsk your question (or type 'exit' to quit): ")
        if query.lower() == 'exit':
            break
        response = process_query(query, df)
        print(response)

        



# In[ ]:




