# Predict the output:
d = {1: "One", 1: "ONE", 2: "Two"}
print(d)

# Why does this happen?

# Solution:
# Output:
{1: 'ONE', 2: 'Two'}

# Explaination: Keys are unique in dict, if same keys are used then most recent key data is getting stored/affected