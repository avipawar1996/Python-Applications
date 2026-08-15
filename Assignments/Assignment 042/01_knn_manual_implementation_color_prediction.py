# Program to implement K-Nearest Neighbors (KNN) manually in Python

"""
Question:
Implement the K-Nearest Neighbors (KNN) algorithm manually in Python
without using any machine learning libraries.

Requirements:
1. Accept X and Y coordinates of a new point from the user.
2. Compute Euclidean distance from all dataset points.
3. Sort the distances.
4. Select K = 3 nearest neighbors.
5. Predict the class label using majority voting.

Dataset:
| Point | X | Y | Label |
|-------|---|---|-------|
| A     | 1 | 2 | Red   |
| B     | 2 | 3 | Red   |
| C     | 3 | 1 | Blue  |
| D     | 6 | 5 | Blue  |

Example Input:
Enter X coordinate: 2
Enter Y coordinate: 2

Expected Output:
Nearest Neighbors:
A - Distance: 1.0
B - Distance: 1.0
C - Distance: 1.41

Predicted Class: Red

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
    ManualKNNClassifier()

if(__name__ == "__main__"):
    main()