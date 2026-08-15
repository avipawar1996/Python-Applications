'''
7. Create a scatter plot of:
StudyHours vs PreviousScore

'''

import pandas as pd
import matplotlib.pyplot as plt

def main():
    df_obj = pd.read_csv("student_performance_ml.csv")

    passed = df_obj[df_obj['FinalResult'] == 1]
    failed = df_obj[df_obj['FinalResult'] == 0]

    plt.scatter(passed['StudyHours'], passed['PreviousScore'], 
                color='green', alpha=0.8, label='Pass')
    plt.scatter(failed['StudyHours'], failed['PreviousScore'], 
                color='red', alpha=0.8, label='Fail')

    plt.xlabel('Study Hours')
    plt.ylabel('Previous Score')
    plt.title('Scatter Plot: StudyHours vs PreviousScore')
    plt.legend()
    plt.show()


if(__name__ == "__main__"):
    main()