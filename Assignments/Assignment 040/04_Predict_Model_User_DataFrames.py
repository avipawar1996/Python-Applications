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

    # Create new dataset with 5 student details and use trained model to predict their results. Display predictions clearly.

    X_new = pd.DataFrame({
        "StudyHours": [5, 7, 12, 9, 6],
        "Attendance": [80, 92, 73, 95, 88],
        "PreviousScore": [60, 75, 76, 85, 68],
        "AssignmentsCompleted": [6, 8, 9, 9, 7],
        "SleepHours": [7, 6, 4, 7, 6]
    })

    y_pred_new = model.predict(X_new)

    X_new["Predictions"] = y_pred_new

    print_border()
    print(X_new)

if(__name__ == "__main__"):
    main()