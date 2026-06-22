# Predict the Output:
s = "python"
print(id(s))

s = s + "3"
print(id(s))
# Explain the reason for change / no change in id()


# Output:
# 2942315380192
# 2942317841840
# Explaination: Strings are immutable, the new strings gets created while updating existing string