'''
Write a python program to implement aa class named Demo with the following specirfications:
    - Class should contain two instance variable: no1 and no2
    - Class should contain one class variable named Value
    - Define a constructor (__init__()) that accepts two parameters and initializes the instance variables.
    - Implement two instance methods:
        Fun() - Display the values of instance variables no1 and no2.
        Gun() - Display the values of no1 and no2.

    - Create two objects of the Demo class as follow:
        Obj1 = Demo(11, 21)
        Obj2 = Demo(51, 101)

    - Call the instance methods in given sequence:
        Obj1.Fun()
        Obj2.Fun()
        Obj1.Gun()
        Obj2.Gun()
'''

class Demo:
    Value = 111

    def __init__(self, no1, no2):
        self.no1, self.no2 = no1, no2
        
    def Fun(self):
        print(f"no1 = {self.no1}             no2 = {self.no1}" )

    def Gun(self):
        print(f"no1 = {self.no1}             no2 = {self.no1}" )

Obj1 = Demo(11, 21)
Obj2 = Demo(51, 101)

Obj1.Fun()
Obj2.Fun()

Obj1.Gun()
Obj2.Gun()