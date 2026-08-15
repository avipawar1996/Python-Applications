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

    y_pred = model.predict(X_test)

    # misclassified students
    misclassified_std = X_test[y_test != y_pred].copy()
    misclassified_std["Actual"] = y_test[y_test != y_pred]
    misclassified_std["Predicted"] = y_pred[y_test != y_pred]

    print_border()
    print(misclassified_std)
    print("Number of misclassified Students: ", len(misclassified_std))

if(__name__ == "__main__"):
    main()