'''
8. Draw a boxplot for Attendance.
Identify if any outliers are present.

'''

import pandas as pd
import matplotlib.pyplot as plt

def main():
    df_obj = pd.read_csv("student_performance_ml.csv")

    plt.boxplot(
        df_obj['Attendance'],
        vert=False, patch_artist=True,
        boxprops=dict(facecolor='lightblue'))
    plt.title('Boxplot of Attendance')
    plt.xlabel('Attendance')
    plt.show()

if(__name__ == "__main__"):
    main()