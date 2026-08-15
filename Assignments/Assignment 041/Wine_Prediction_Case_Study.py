import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def print_border():
    print("-" * 80)

def WinePredictor():

    # -----------------------------------------------------------------------
    # ------------------------- Loading of Data Set -------------------------
    # -----------------------------------------------------------------------

    df = pd.read_csv("WinePredictor.csv")

    # -----------------------------------------------------------------------
    # -------------------------- Analysing DataSet --------------------------
    # -----------------------------------------------------------------------
    # Data Analysis
    # print_border()
    # print("First 5 rows: ", df.head())
    # print_border()
    # print("Last 5 rows: ", df.tail())
    # print_border()

    # -----------------------------------------------------------------------
    # -------------------------- Cleaning Data Set --------------------------
    # -----------------------------------------------------------------------
    df = df.dropna()

    # -----------------------------------------------------------------------
    # -------------------- Splitting Features and Labels --------------------
    # -----------------------------------------------------------------------

    X = df.drop(["Class"], axis=1)
    Y = df["Class"]

    # -----------------------------------------------------------------------
    # --------------------------- Encoding Labels------------ ---------------
    # -----------------------------------------------------------------------

    # Dataset already encoded in numbers
    # encoder = LabelEncoder
    # y = encoder.fit_transform(y)

    # -----------------------------------------------------------------------
    # --------------- Splitting Data for training and testing ---------------
    # -----------------------------------------------------------------------

    X_train, X_test, y_train, y_test = train_test_split(X, Y, random_state=42, test_size=0.3)

    # -----------------------------------------------------------------------
    # -------------- Creating the DecisionTreeClassifier model --------------
    # -----------------------------------------------------------------------

    model = DecisionTreeClassifier(random_state=42)

    # -----------------------------------------------------------------------
    # ------------------------ Training of the model ------------------------
    # -----------------------------------------------------------------------

    model = model.fit(X_train, y_train)

    # -----------------------------------------------------------------------
    # -------------------------- Testing the model --------------------------
    # -----------------------------------------------------------------------
    y_pred = model.predict(X_test)

    # -----------------------------------------------------------------------
    # ------------------------ Accuracy  Calculation ------------------------
    # -----------------------------------------------------------------------
    # model_accuracy = model.score(X_test, y_test)
    model_accuracy = accuracy_score(y_test, y_pred)
    print_border()
    print(f"Model Accuracy: {model_accuracy * 100 :.2f}")
    print_border()

def main():
    WinePredictor()

if(__name__ == "__main__"):
    main()