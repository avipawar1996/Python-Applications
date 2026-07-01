# Question: -> Write a program which accepts marks and display the grade:
# >= 75 -> Distinction
# >= 60 -> First Class
# >= 50 -> Second Class
# < 50 -> Fail
# Solution:

# ----------------------------------------------------------------------------

def FindGrade(marks):
    if(marks >= 75): return "Distinction"
    elif(marks >= 60): return "First Class"
    elif(marks >= 50): return "Second Class"
    elif(marks < 50): return "Fail"

def main():
    marks = int(input("Enter the marks: "))
    grade = FindGrade(marks)
    print("Grade is: ", grade)

if(__name__ == "__main__"):
    main()