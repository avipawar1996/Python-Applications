'''
3. Using pandas functions, calculate and display:
    Average StudyHours
    Average Attendance
    Maximum PreviousScore
    Minimum SleepHours

'''

import pandas as pd

def main():
    df_obj = pd.read_csv("student_performance_ml.csv")

    print("Average StudyHours: ", df_obj["StudyHours"].mean())
    print("Average Attendance: ", df_obj["Attendance"].mean())
    print("Maximum PreviousScore: ", (df_obj["PreviousScore"].max()))
    print("Minimum SleepHours: ", (df_obj["SleepHours"].min()))

if(__name__ == "__main__"):
    main()