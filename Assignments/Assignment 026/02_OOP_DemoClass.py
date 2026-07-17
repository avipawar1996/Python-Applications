'''
Write a python program to implement aa class named Circle with the following requirements:
    - Class should contain three instance variable: Radius, Area and Circumference
    - Class should contain one class variable named PI initialized to 3.14
    - Define a constructor (__init__()) that initializes all instance variables to 0.0.

    - Implement two instance methods:
        Accept()        - Accept the radius of the circle from the user
        CalculateArea() - Calculate the area of the circle and store it in the Area variable.
        Circumference() - Calculate the circumference of the circle and store it in the Circumference variable.
        Display()       - Displays the value of Radius, Area, and Circumference

    - Create multiple objects of the Circle and invoke all the instance methods for each object
'''

class Circle:

    PI = 3.14

    def __init__(self):
        self.Radius, self.Area, self.Circumference = [ 0.0, 0.0, 0.0]
        
    def Accept(self):
        try:
            print("\n-------------------------------------------------")
            self.Radius = float(input("Enter the Radius of circle: "))

        except ValueError as v:
            print("could not convert string to float: ", v)
            if(input("Want to retry?(y/n): ") == "y"):
                self.Accept()
            else:
                print("Aborting the action.")
                return

    def CalculateArea(self): self.Area = Circle.PI * (self.Radius ** 2)

    def CalculateCircumference(self): self.Circumference = 2 * Circle.PI * self.Radius

    def Display(self):
        print(f"\nFor the circle with Radius {self.Radius} cm:\nArea = {self.Area:.2f} sq.cm \nCircumference = {self.Circumference:.2f} cm")
        print("-------------------------------------------------")


Obj1 = Circle()
Obj1.Accept()
Obj1.CalculateArea()
Obj1.CalculateCircumference()
Obj1.Display()

Obj2 = Circle()
Obj2.Accept()
Obj2.CalculateArea()
Obj2.CalculateCircumference()
Obj2.Display()

Obj3 = Circle()
Obj3.Accept()
Obj3.CalculateArea()
Obj3.CalculateCircumference()
Obj3.Display()

Obj4 = Circle()
Obj4.Accept()
Obj4.CalculateArea()
Obj4.CalculateCircumference()
Obj4.Display()