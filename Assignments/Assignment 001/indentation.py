# This is a simple Python program to demonstrate indentation

# 1. Syntactical error:
# Correct expected:
print("Jay Ganesh")
print("Start Coding")

# Syntactical error (wrong indentation):
print("Jay Ganesh")
    # print("Start Coding") #This line is indented incorrectly, it will cause a syntax error


# ---------------------------------------------------------------------

# 2. Logical error:
# Correct expected:
age = int(input("Enter your age: "))
if age >= 18:
    print("You can adult.")
    print("You can drive, apply for a driving license.")  

# Logical Error:
if age >= 18:
    print("You can adult.") # This line is indented correctly within the if block
print("You can drive, apply for a driving license.") # This line is not indented properly, so it will execute always