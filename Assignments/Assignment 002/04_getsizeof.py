# Question 04:
# What is use of getsizeof() ?

# Solution: getsizeof() is used to get the amount of memry occupied by variable in bytes
from sys import getsizeof

a = 12
print("Memory occupied by a: ", getsizeof(a), " Bytes") 

# Output: 
# Memory occupied by a:  28  Bytes