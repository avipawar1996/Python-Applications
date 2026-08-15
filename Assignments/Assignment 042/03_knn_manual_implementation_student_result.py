#  Use KNN to predict whether a student passes or fails based on study hours and attendance.

"""
Question 3
Use KNN to predict whether a student passes or fails based on study hours and attendance.

Dataset:

Study Hours	Attendance	Result
2	60	Fail
5	80	Pass
6	85	Pass
1	50	Fail


Tasks
Accept input from user:
Study hours
Attendance percentage
Apply KNN algorithm
Predict whether the student Passes or Fails

Input Example
Enter Study Hours: 4
Enter Attendance: 70
Expected Output

Predicted Result: Pass
"""
import math

def calc_euclidean_distance(p1, p2):
    return round(math.sqrt(((p2["study_hours"] - p1["study_hours"]) ** 2) +
                           ((p2["attendance"] - p1["attendance"]) ** 2)), 2)

def get_k_nearest_neighbors(distances, k=3):
    distances.sort(key=lambda d: d["distance"])
    return distances[:k]

def ManualKNNClassifier(k=3):
    dataset = [
        {"study_hours": 2, "attendance": 60, "result": "Fail"},
        {"study_hours": 5, "attendance": 80, "result": "Pass"},
        {"study_hours": 6, "attendance": 85, "result": "Pass"},
        {"study_hours": 1, "attendance": 50, "result": "Fail"}
    ]

    new_point = {
        "study_hours": float(input("Enter Study Hours: ")),
        "attendance": float(input("Enter Attendance: "))
    }

    distances = []
    for data in dataset:
        dist = calc_euclidean_distance(new_point, data)
        distances.append({
            "study_hours": data["study_hours"],
            "attendance": data["attendance"],
            "distance": dist,
            "result": data["result"]
        })

    neighbors = get_k_nearest_neighbors(distances, k)
    results = [neighbor["result"] for neighbor in neighbors]
    predicted_result = max(set(results), key=results.count)

    print("Nearest Neighbors:")
    for neighbor in neighbors:
        print(f"Study Hours: {neighbor['study_hours']}, Attendance: {neighbor['attendance']}, Distance: {neighbor['distance']}, Result: {neighbor['result']}")
    print(f"Predicted Result: {predicted_result}")

def main():
    ManualKNNClassifier()

if __name__ == "__main__":
    main()
