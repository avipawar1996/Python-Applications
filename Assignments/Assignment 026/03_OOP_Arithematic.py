'''
Write a python program to implement aa class named Arithematic with the following requirements:
    - Class should contain three instance variable: Value1 and Value2
    - Define a constructor (__init__()) that initializes all instance variables to 0

    - Implement two instance methods:
        Accept()         - Accept values for Value1 and Value2 from the user
        Addition()       - return the addition of Value1 and Value2
        Substraction()   - return the substraction of Value1 and Value2
        Multiplication() - return the multiplication of Value1 and Value2
        Division()       - return the division of Value1 and Value2
        
    - Create multiple objects of the Arithematic class and invoke all the instance methods
'''

class Arithematic:

    def __init__(self):
        self.Value1, self.Value2 = 0, 0
        
    def Accept(self):
        try:
            print("\n-------------------------------------------------")
            self.Value1 = int(input("Enter the first number: "))
            self.Value2 = int(input("Enter the second number: "))
            print()

        except ValueError as v:
            print("could not convert string to int: ", v)
            if(input("Want to retry?(y/n): ") == "y"):
                self.Accept()
            else:
                print("Aborting the action.")
                return

    def Addition(self): return self.Value1 + self.Value2
    def Substraction(self): return self.Value1 - self.Value2
    def Multiplication(self): return self.Value1 * self.Value2
    def Division(self): return self.Value1 / self.Value2


Obj1 = Arithematic()
Obj1.Accept()
print(f"{Obj1.Value1} + {Obj1.Value2} = {Obj1.Addition()}")
print(f"{Obj1.Value1} - {Obj1.Value2} = {Obj1.Substraction()}")
print(f"{Obj1.Value1} * {Obj1.Value2} = {Obj1.Multiplication()}")
print(f"{Obj1.Value1} / {Obj1.Value2} = {Obj1.Division():.2f}")
print("-------------------------------------------------")

Obj2 = Arithematic()
Obj2.Accept()
print(f"{Obj2.Value1} + {Obj2.Value2} = {Obj2.Addition()}")
print(f"{Obj2.Value1} - {Obj2.Value2} = {Obj2.Substraction()}")
print(f"{Obj2.Value1} * {Obj2.Value2} = {Obj2.Multiplication()}")
print(f"{Obj2.Value1} / {Obj2.Value2} = {Obj2.Division():.2f}")
print("-------------------------------------------------")

Obj3 = Arithematic()
Obj3.Accept()
print(f"{Obj3.Value1} + {Obj3.Value2} = {Obj3.Addition()}")
print(f"{Obj3.Value1} - {Obj3.Value2} = {Obj3.Substraction()}")
print(f"{Obj3.Value1} * {Obj3.Value2} = {Obj3.Multiplication()}")
print(f"{Obj3.Value1} / {Obj3.Value2} = {Obj3.Division():.2f}")
print("-------------------------------------------------")

Obj4 = Arithematic()
Obj4.Accept()
print(f"{Obj4.Value1} + {Obj4.Value2} = {Obj4.Addition()}")
print(f"{Obj4.Value1} - {Obj4.Value2} = {Obj4.Substraction()}")
print(f"{Obj4.Value1} * {Obj4.Value2} = {Obj4.Multiplication()}")
print(f"{Obj4.Value1} / {Obj4.Value2} = {Obj4.Division():.2f}")
print("-------------------------------------------------")