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

    # Model accuracy calculation - Manual and sklearn

    y_pred = model.predict(X_test)
    accuracy_score_sklearn = model.score(X_test, y_test)
    accuracy_score_manual = sum( pred == test for pred, test in zip(y_pred, y_test))/len(y_pred)
    print_border()
    print("sklearn accuracy: ", accuracy_score_sklearn * 100)
    print("Manual accuracy: ", accuracy_score_manual * 100)

if(__name__ == "__main__"):
    main()