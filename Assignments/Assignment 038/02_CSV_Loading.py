'''
2. Write a program to:
    Display total number of students in the dataset
    Count how many students Passed (FinalResult = 1)
    Count how many students Failed (FinalResult = 0)
'''

import pandas as pd

def main():
    df_obj = pd.read_csv("student_performance_ml.csv")

    print("Total number of students: ", df_obj.shape[0])
    print("Total number of passed students: ", (df_obj["FinalResult"]==1).sum())
    print("Total number of failed students: ", (df_obj["FinalResult"]==0).sum())

if(__name__ == "__main__"):
    main()