# Predict the output:

lst = [10, 20, 30]
tpl = (10, 20, 30)

lst[0] = 100  # This will work, as lists are mutable
tpl[0] = 100  # This will not work, as tuples are immutable

# Output:
# TypeError: 'tuple' object does not support item assignment