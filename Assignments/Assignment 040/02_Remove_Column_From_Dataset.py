from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pandas as pd

print_border = lambda : print("-" * 70)

def main():
    df = pd.read_csv("student_performance_ml.csv")
    X = df.drop(["FinalResult", "SleepHours"], axis=1)
    Y = df["FinalResult"]

    X_train, X_test, y_train, y_test = train_test_split(X, Y, random_state=42, test_size=0.3)
    model = DecisionTreeClassifier(random_state=42)
    model = model.fit(X_train, y_train)

    model_accuracy = model.score(X_test, y_test)

    # Remove column SleepHours from dataset to train model and check accuracy

    X_train, X_test, y_train, y_test = train_test_split(X, Y, random_state=42, test_size=0.3)
    model = model.fit(X_train, y_train)
    model_accuracy = model.score(X_test, y_test)

    print_border()
    print(f"Model Accuracy with all column: {model_accuracy * 100 :.2f} %")
    print(f"Model Accuracy removing 'SleepHours' column: {model_accuracy * 100 :.2f} %")
    print(f"Model Accuracy difference 'All features' v/s Accuracy by removing 'SleepHours': {model_accuracy - model_accuracy :.2f}")


if(__name__ == "__main__"):
    main()