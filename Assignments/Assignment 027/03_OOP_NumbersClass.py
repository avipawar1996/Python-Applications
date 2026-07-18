'''
Write a python program to implement a class named Numbers with the following specifications:
    - Class should contain one instance variable: value
    - Define a constructor (__init__()) that accept number from user and initialize : value.
    - Implement an instance methods:
        ChkPrime()   - Return True if number is prime otherwise False
        ChkPerfect() - Return True if number is perfect otherwise False
        Factors()    - Display all factors of number
        SumFactors() - returns the sum of all factors of number

    - Create multiple objects and demonstrate all methods.
'''

class Numbers:

    def __init__(self, number:int):
        self.value = number

    def ChkPrime(self):
        if([0, 1].__contains__(self.value) ):
            return False
        else:
            for i in range(2, int(self.value/2)+1):
                if(self.value % 2 == 0):
                    return False
            return True
        
    def ChkPerfect(self):
        facts = self.findFactors()
        if(len(facts)>1):
            facts.pop()
        else: return False
        if(self.value == sum(facts)):
            return True
        else: return False
    
    def SumFactors(self): return sum(self.findFactors())

    def Factors(self): return self.findFactors()
    
    def findFactors(self):
        if(self.value == 1):
            return [1]
        if(self.value > 1):
            facts = [1]
            for i in range(2, self.value + 1):
                if (self.value % i == 0):
                    facts.append(i)
            return facts

value = int(input("Enter the number: "))

obj1 = Numbers(value)
isPrime = obj1.ChkPrime()
isPerfect = obj1.ChkPerfect()
factors = obj1.findFactors()
sumFactors = obj1.SumFactors()

print(f"Is {obj1.value} a Prime? : {isPrime}")
print(f"Is {obj1.value} a Perfect Number? : {isPerfect}")
print(f"Sum of Factors of {obj1.value} : {sumFactors}")

print(f"Factors of {obj1.value}: ", end="   ")
for fact in factors:
    print(fact, end="    ")

print("\n-------------------------------------------------")
