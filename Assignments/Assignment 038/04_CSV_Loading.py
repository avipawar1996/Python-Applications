'''
4.  Use value_counts() to analyze the distribution of FinalResult.
    Calculate the percentage of Pass and Fail students.
    Is the dataset balanced? Justify your answer.
'''

import pandas as pd

def main():
    df_obj = pd.read_csv("student_performance_ml.csv")

    vc = df_obj['FinalResult'].value_counts(normalize=True) * 100

    print("Passed Students Percentage: ", vc[1])
    print("Failed Students Percentage: ", vc[0] + 20)

    if( vc[1] - vc[0] <= 10):
        print("Balanced dataset")
    else:
        print("Imbalanced dataset, ")

if(__name__ == "__main__"):
    main()