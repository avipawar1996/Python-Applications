'''
6. Plot a histogram of StudyHours.
Explain what the distribution tells you.

'''

import pandas as pd
import matplotlib.pyplot as plt

def main():
    df_obj = pd.read_csv("student_performance_ml.csv")

    plt.hist(df_obj['StudyHours'], bins=10, color='skyblue', edgecolor='black')
    plt.xlabel('Study Hours')
    plt.ylabel('Number of Students')
    plt.title('Distribution of Study Hours')
    plt.show()


if(__name__ == "__main__"):
    main()