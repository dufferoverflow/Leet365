# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward.
# For example, 121 is a palindrome while 123 is not.

# Example 1:
# Input: x = 121
# Output: true

# Example 2:
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

# Example 3:
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

# Example 4:
# Input: x = -101
# Output: false
 

# Constraints:
# -231 <= x <= 231 - 1

# Observations:
# 1. All negative numbers are NOT palindromes
# 2. Digit = dup % 10

def solution_n(x):
    
    if x < 0:
        return False
    
    y = 0
    dup = int(x)
    while dup >= 1:
        y = (y * 10) + (dup % 10)
        dup = dup//10
    
    if y == x:
        return True
    
    return False

tests = [
    {
        'x': 121,
        'output': True
    },
    {
        'x': -121,
        'output': False
    },
    {
        'x': 10,
        'output': False
    },
    {
        'x': -101,
        'output': False
    }
]

counter = 1
for test in tests:
    if test['output'] == solution_n(test['x']):
        print(f"Test Case {counter} Passed!")
    else:
        print(f"Test Case {counter} Failed!")
        print(f"Input: {test['x']}")
        print(f"Expected Output: {test['output']}")
        print(f"Obtained Output: {solution_n(test['x'])}")
    
    print()
    counter += 1