# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
# Increment the large integer by one and return the resulting array of digits.

# Example 1:
# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].

# Example 2:
# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].

# Example 3:
# Input: digits = [0]
# Output: [1]
# Explanation: The array represents the integer 0.
# Incrementing by one gives 0 + 1 = 1.
# Thus, the result should be [1].

# Example 4:
# Input: digits = [9]
# Output: [1,0]
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0].
 

# Constraints:
# 1 <= digits.length <= 100
# 0 <= digits[i] <= 9
# digits does not contain any leading 0's.

tests = [
    {
        'digits': [1,2,3],
        'output': [1,2,4]
    },
    {
        'digits': [4,3,2,1],
        'output': [4,3,2,2]
    },
    {
        'digits': [0],
        'output': [1]
    },
    {
        'digits': [9],
        'output': [1,0]
    }
]

def solution(digits):
    i = len(digits) - 1

    while i >= 0:
        digit = digits[i]
        digits[i] = (digit + 1) % 10

        if digit + 1 < 10:
            return digits
        i -= 1

    return ([1] + digits)

counter = 1
for test in tests:
    if test['output'] == solution(test['digits']):
        print(f"Test Case {counter} Passed!")
    else:
        print(f"Test Case {counter} Failed!")
        print(f"Input: {test['digits']}")
        print(f"Expected Output: {test['output']}")
        print(f"Obtained Output: {solution(test['digits'])}")
    
    print()
    counter += 1
