from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
from multiprocessing import Pool

print_border = lambda : print("-" * 70)

def tune_model(_random_state):
    df = pd.read_csv("student_performance_ml.csv")
    X = df.drop(["FinalResult"], axis=1)
    Y = df["FinalResult"]
    X_train, X_test, y_train, y_test = train_test_split(X, Y, random_state=42, test_size=0.3)

    model = DecisionTreeClassifier(random_state=_random_state)
    model = model.fit(X_train, y_train)
    accuracy_score = model.score(X_test, y_test)

    return (_random_state, accuracy_score)

def main():
    random_states = [0, 10, 42]

    with Pool(processes=len(random_states)) as pool:
        accuracies = pool.map(tune_model, random_states)

    for rs, acc in accuracies:
        print_border()
        print(f"Random state {rs}: Test Accuracy = {acc*100:.2f}%")

if(__name__ == "__main__"):
    main()