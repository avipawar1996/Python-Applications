# Write a Python program to show how KNN predictions change when the value of K varies (K = 1, 3, 5).

"""
The value of K plays an important role in the KNN algorithm.
Write a Python program that demonstrates how prediction changes when K changes.

Dataset:
Use the same dataset as Assignment 1.

Tasks:
Predict the class of the same new point using:

K = 1
K = 3
K = 5

Show the prediction results for each case.
Explain why the prediction changes when K increases.
Expected Output:
"""

import math

def calc_euclidean_distance(p1, p2):
    return math.sqrt( ((p2["x"] - p1["x"]) ** 2) +( (p2["y"] - p1["y"]) ** 2))

def get_k_nearest_neighbors(distances, k=3):
    distances.sort(key=lambda d: d["distance"])
    return distances[:k]

def ManualKNNClassifier(k=3):
    df = [
        {"point": "A", "x": 1, "y": 2, "label": "Red"},
        {"point": "B", "x": 2, "y": 3, "label": "Red"},
        {"point": "C", "x": 3, "y": 1, "label": "Blue"},
        {"point": "D", "x": 6, "y": 5, "label": "Blue"}
    ]

    new_point = {
        "point" : "NEW",
        "x" : float(input("Enter x coordinate: ")),
        "y" : float(input("Enter x coordinate: "))
    }

    distances = []

    for series in df:
        dist = calc_euclidean_distance(new_point, series)
        distances.append({
            "point": series["point"],
            "distance": dist,
            "label": series["label"]
        })

    neighbors = get_k_nearest_neighbors(distances, k)
    labels = [neighbor["label"] for neighbor in neighbors]
    predicted_class = max(set(labels), key=labels.count)

    print("Predicted class: ", predicted_class)

def main():
    k = int(input("Enter the value of k: "))
    ManualKNNClassifier(k)

if(__name__ == "__main__"):
    main()