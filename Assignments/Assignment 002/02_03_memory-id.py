# Question 02:  What is difference between:
# a = 10
# b = 10
# and 
# a = [10]
# b = [10]
# Explain with id() function

# Question 03: What does id() function return? Is the value returned by id() same for 2 variables holding same value

# Solution:
a = 10
b = 10
print("Memory address of a: ", id(a))
print("Memory address of b: ", id(b))

# Output:
# Memory address of a:  140709082613144 
# Memory address of b:  140709082613144

# both shows same value as both are int i.e. numeric (immutable) so share the same value object reference

a = [10]
b = [10]
print("Memory address of a: ", id(a))
print("Memory address of b: ", id(b))

# Output:
# Memory address of a:  1686406674496
# Memory address of b:  1686406558016

# both shows different value as both are list i.e. sequence (immutable) so saperate memory is allocated for the variables