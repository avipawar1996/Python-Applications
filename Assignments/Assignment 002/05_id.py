# Question 05:
# Predict the output: 
# a = 10
# b = 10
# print (id(a) == id(b))
# And explain why does this happens

# Solution:
a = 10
b = 10
print (id(a) == id(b))

# Output:
True

# Explaination: Because both a and b are int (immutable) data types holding same value, they both shares reference to the object of same value i.e. 10 and output is True