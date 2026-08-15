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

    accuracy_score = model.score(X_test, y_test)
    print_border()
    print("Model Accuracy without PerformanceIndex: ", accuracy_score * 100)

    # Add column dynamically
    df["PerformanceIndex"] = (df["StudyHours"] * 2) + df["Attendance"]
    X = df.drop(["FinalResult"], axis=1)
    Y = df["FinalResult"]

    X_train, X_test, y_train, y_test = train_test_split(X, Y, random_state=42, test_size=0.3)

    model = DecisionTreeClassifier(random_state=42)
    model = model.fit(X_train, y_train)

    accuracy_score_pi = model.score(X_test, y_test)

    print_border()
    print("Model Accuracy with PerformanceIndex: ", accuracy_score_pi * 100)
    print_border()

if(__name__ == "__main__"):
    main()