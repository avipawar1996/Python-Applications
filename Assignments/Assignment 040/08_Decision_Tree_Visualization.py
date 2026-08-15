from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn import tree
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv("student_performance_ml.csv")
    X = df.drop(["FinalResult"], axis=1)
    Y = df["FinalResult"]
    X_train, X_test, y_train, y_test = train_test_split(X, Y, random_state=42, test_size=0.3)

    model = DecisionTreeClassifier(random_state=42)
    model = model.fit(X_train, y_train)

    tree.plot_tree(
        decision_tree=model,
        feature_names=X.columns,
        class_names=["Fail", "Pass"],
        filled=True,
        rounded=True
        )
    plt.show()

    root_feature_index = model.tree_.feature[0]
    print("Root index: ", root_feature_index)
    print(f"Root Feature: {X.columns[root_feature_index]}")

if(__name__ == "__main__"):
    main()