'''
9. Create a plot showing relationship between AssignmentsCompleted and FinalResult.
Explain your observation.

'''

import pandas as pd
import matplotlib.pyplot as plt

def main():
    df_obj = pd.read_csv("student_performance_ml.csv")

    passed = df_obj[df_obj['FinalResult'] == 1]
    failed = df_obj[df_obj['FinalResult'] == 0]

    plt.scatter(passed['AssignmentsCompleted'], passed['FinalResult'],
                color='green', alpha=0.6, label='Pass')
    plt.scatter(failed['AssignmentsCompleted'], failed['FinalResult'],
                color='red', alpha=0.6, label='Fail')

    plt.xlabel('Assignments Completed')
    plt.ylabel('Final Result (0=Fail, 1=Pass)')
    plt.title('Assignments Completed vs FinalResult')
    plt.legend()
    plt.show()

if(__name__ == "__main__"):
    main()