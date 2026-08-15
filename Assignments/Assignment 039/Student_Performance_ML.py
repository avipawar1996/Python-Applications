from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import pandas as pd

def main():

    df = pd.read_csv("student_performance_ml.csv")
    X = df.drop(["FinalResult"], axis=1)
    Y = df["FinalResult"]
    X_train, X_test, y_train, y_test = train_test_split(X, Y, random_state=42, test_size= 0.5)

    """
    1. Create model object and train using fit
    """
    model = DecisionTreeClassifier()
    model = model.fit(X_train, y_train)

    """
    2. Test model on X_test and display predicted values along with actual values
    """
    y_pred = model.predict(X_test)

    for i in range(len(y_pred)):
        print(f" Predicted: {y_pred[i]} --------- Actual: {y_test.iloc[i]}")

    """
    3. Calculate Model accuracy using accuracy_score and display result in % format
    """
    accuracy = accuracy_score(y_test, y_pred)
    print(f" Accuracy: {accuracy * 100:.2f} %")

    """
    4. Generate ConfusionMatrix and display it using ConfusionMatrixDisplay
        Explain clearly:
                True Positive
                True Negative
                False Positive
                False Negative
    """


    cm = confusion_matrix(y_test, y_pred)
    cm_disp = ConfusionMatrixDisplay(confusion_matrix=cm)
    cm_disp.plot()
    labels = [
        "TN\n(actual failed === predicted failed)",
        "FP\n(actual failed === predicted passed)",
        "FN\n(actual passed === predicted failed)",
        "TP\n(actual passed === predicted passed)"
    ]
    positions = [(0,0), (1,0), (0,1), (1,1)]

    for label, (x,y) in zip(labels, positions):
        plt.text(x, y-0.25, label, ha="center", va="top", color="white", fontsize=8)
    plt.show()

    """
    5. Calculate training accuracy and testing accuracy
    """
    train_accuracy = model.score(X_train, y_train)
    test_accuracy = model.score(X_test, y_test)

    print(f" Training accuracy: {train_accuracy * 100:.2f} %")
    print(f" Testing accuracy: {test_accuracy * 100:.2f} %")

    # condition checks for model fitting
    if train_accuracy > 0.95 and (train_accuracy - test_accuracy) > 0.10:
        print(" Model is Overfitting")
    elif train_accuracy < 0.70 and test_accuracy < 0.70:
        print(" Model is Underfitting")
    elif abs(train_accuracy - test_accuracy) <= 0.05:
        print(" Model is a Good Fit")
    else:
        print(" Model needs further tuning")

    """
    6: Training three Decision Tree models with different depths.
    """
    # Model depth = 1
    model = DecisionTreeClassifier(max_depth=None, random_state=42)
    model = model.fit(X_train, y_train)
    acc = model.score(X_test, y_test)
    print(f"Model accuracy with depth = 1 is: {(acc * 100) :.2f}")

    # Model depth = 2
    model = DecisionTreeClassifier(max_depth=2, random_state=42)
    model = model.fit(X_train, y_train)
    acc = model.score(X_test, y_test)
    print(f"Model accuracy with depth = 2 is: {(acc * 100) :.2f}")

    # Model depth = 3
    model = DecisionTreeClassifier(max_depth=3, random_state=42)
    model = model.fit(X_train, y_train)
    acc = model.score(X_test, y_test)
    print(f"Model accuracy with depth = 3 is: {(acc * 100) :.2f}")

    """
    7: Predicting the student’s result using the trained model.
    """

    test_data = [[6, 85, 66, 7, 7]]

    model = DecisionTreeClassifier(random_state=42)
    model = model.fit(X_train, y_train)
    prediction = model.predict(test_data)
    if prediction[0]== 1:
        passing_status = "Passed"
    else:
        passing_status = "Failed"
    print(passing_status)

if(__name__ == "__main__"):
    main()