MakeNumDbl = lambda num : num * 2
CompareNum = lambda num1, num2 : num1 if num1 > num2 else num2
def checkIfPrime(num):
    for i in range(2, int(num/2)+1):
        if(num % i == 0):
            return False
    return True