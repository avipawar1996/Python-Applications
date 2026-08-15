from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pandas as pd

print_border = lambda : print("-" * 70)

def main():
    df = pd.read_csv("student_performance_ml.csv")
    X = df.drop(["FinalResult"], axis=1)
    Y = df["FinalResult"]

    X_train, X_test, y_train, y_test = train_test_split(X, Y, random_state=42, test_size=0.2)
    model = DecisionTreeClassifier(random_state=42)
    model = model.fit(X_train, y_train)

    train_acc = model.score(X_train, y_train) * 100
    test_acc = model.score(X_test, y_test) * 100

    print(f"Training Accuracy: {test_acc :.2f}")
    print_border()
    print(f"Testing  Accuracy: {train_acc :.2f}")
    print_border()

if(__name__ == "__main__"):
    main()