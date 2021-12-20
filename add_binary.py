# Given two binary strings a and b, return their sum as a binary string. 

# Example 1:
# Input: a = "11", b = "1"
# Output: "100"

# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"

# Constraints:
# 1 <= a.length, b.length <= 104
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.

tests = [
    {
        'a': "11",
        'b': "1",
        'sum': "100"
    },
    {
        'a': "1010",
        'b': "1011",
        'sum': "10101"
    }
]

def solution(a,b):
    #normalise the strings
    if len(a) < len(b):
        a = "0" * (len(b) - len(a)) + a
    if len(b) < len(a):
        b = "0" * (len(a) - len(b)) + b 
    
    sum = ""
    carry = 0
    i = len(a) - 1
    while i >= 0:
        addition = int(a[i]) + int(b[i]) + carry
        sum = str(addition % 2) + sum
        carry = addition // 2
        i -= 1

    if carry == 1:
        sum = "1" + sum 
    
    return sum

counter = 1
for test in tests:
    if test['sum'] == solution(test['a'], test['b']):
        print(f"Test Case {counter} Passed!")
    else:
        print(f"Test Case {counter} Failed!")
    
    print()
    counter += 1