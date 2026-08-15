'''
5. Based on the dataset values, analyze whether:
    Higher StudyHours increase the chance of passing.
    Higher Attendance improves FinalResult.

    Write your observations in 4 to 5 lines.

'''

import pandas as pd

def main():
    df_obj = pd.read_csv("student_performance_ml.csv")

    avg_study_hours = df_obj.groupby("FinalResult")["StudyHours"].mean()
    avg_attendance = df_obj.groupby("FinalResult")["Attendance"].mean()

    if avg_study_hours[1] > avg_study_hours[0]:
        print("\nObservation: Higher StudyHours increase chance of passing.")
    else:
        print("\nObservation: StudyHours do not show improvement in passing.")

    if avg_attendance[1] > avg_attendance[0]:
        print("Observation: Higher Attendance improves FinalResult.")
    else:
        print("Observation: Attendance does not show improvement in FinalResult.")

if(__name__ == "__main__"):
    main()