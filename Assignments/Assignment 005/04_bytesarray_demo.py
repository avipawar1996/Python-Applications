# Predict the output:
ba = bytearray([65,55,57])
ba[0] = 97
print(ba)
# Is this allowed?

# Solution:
# Output:
# b'aBC'
# As bytearray is mutable in nature, the update is allowed to its values and hence 65 (ASCII char A) is converted to a as decimal equivalent of ASCII 'a' is 97)