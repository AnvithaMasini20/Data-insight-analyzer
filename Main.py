#!/usr/bin/env python
# coding: utf-8

# In[1]:


import Cleaning_and_Loading as CL
import Query_Processing as QP

if __name__ == "__main__":
    file_path = input("Enter the file path of your dataset: ")
    df = CL.load_data(file_path)
    df = CL.clean_data(df)
    
    print("Data Loaded Successfully! Here's a preview:")
    print(df.head())

    while True:
        query = input("\nAsk your question (or type 'exit' to quit): ")
        if query.lower() == 'exit':
            break
        response = QP.process_query(query, df)
        print(response)


# In[ ]:


Tumor_Detection.csv


# In[ ]:




