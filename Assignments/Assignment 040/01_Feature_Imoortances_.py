from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pandas as pd

print_border = lambda : print("-" * 70)

def main():
    df = pd.read_csv("student_performance_ml.csv")
    X = df.drop(["FinalResult"], axis=1)
    Y = df["FinalResult"]

    X_train, X_test, y_train, y_test = train_test_split(X, Y, random_state=42, test_size=0.3)
    model = DecisionTreeClassifier(random_state=42)
    model = model.fit(X_train, y_train)

    model_accuracy = model.score(X_test, y_test)
    mf = model.feature_importances_

    # csv columns: StudyHours,Attendance,PreviousScore,AssignmentsCompleted,SleepHours,FinalResult

    print_border()
    print(f"Importance_ value of 'StudyHours': {mf[0]:.4f}")
    print(f"Importance_ value of 'Attendance': {mf[1]:.4f}")
    print(f"Importance_ value of 'PreviousScore': {mf[2]:.4f}")
    print(f"Importance_ value of 'AssignmentsCompleted': {mf[3]:.4f}")
    print(f"Importance_ value of 'SleepHours': {mf[4]:.4f}")

if(__name__ == "__main__"):
    main()