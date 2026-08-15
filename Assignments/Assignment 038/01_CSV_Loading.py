'''
Write  a python program to load the file student_performance_ml.csv using pandas.
Display:
    First 5 records
    Last 5 records
    Total number of rows and columns
    List of column names
    Data type of each column
'''

import pandas as pd

def main():
    df_obj = pd.read_csv("student_performance_ml.csv")

    print("First 5 rows: \n", df_obj.head())
    print("Last 5 rows: \n", df_obj.tail())

    print("Total number of rows: ", df_obj.shape[0])
    print("Total number of columns: ", df_obj.shape[1])

if(__name__ == "__main__"):
    main()