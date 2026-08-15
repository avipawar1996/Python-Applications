import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import seaborn as sns

def main():

    # # 1. Dataset Loading
    df = pd.read_csv("student_performance_ml.csv")

    # 2. Data Analysis
    print("Dataset Tail: \n", df.head())
    print("Dataset Tail: \n", df.tail())
    df.info()
    print("Dataset Description: \n", df.describe())

    # 3. Data Visualization
    plt.plot(df)
    plt.show()

    # 4. split training and testing data
    X = df.drop(["FinalResult"], axis=1)
    Y = df["FinalResult"]
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3)

    # 5. Training the model
    model = DecisionTreeClassifier(random_state=42)
    model = model.fit(X_train, y_train)

    # 6. Testing predictions
    y_pred = model.predict(X_test)

    # 7. Accuracy Calculation
    acc = accuracy_score(y_test, y_pred)
    print(f"Model accuracy is: {acc * 100 :.2f}")

    # 8. Confusion Matrix Generation
    cm = confusion_matrix(y_test, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["Fail", "Pass"])
    disp.plot(cmap="Blues")
    plt.title("Confusion Matrix")
    plt.show()

    # Step 9: Final conclusion
    if acc > 0.85:
        print("Conclusion: Model responds well.")
    elif acc < 0.60:
        print("Conclusion: Model is underfitting.")
    else:
        print("Conclusion: Model may need tuning.")

if (__name__ == "__main__"):
    main()