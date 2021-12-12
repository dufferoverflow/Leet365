# Given two integers dividend and divisor, divide two integers without using multiplication or division operator.

# The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

# Return the quotient after dividing dividend by divisor.

# Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−2^31, 2^31 − 1]. For this problem, if the quotient is strictly greater than 2^31 - 1, then return 2^31 - 1, and if the quotient is strictly less than -2^31, then return -2^31.

# Example 1:
# Input: dividend = 10, divisor = 3
# Output: 3
# Explanation: 10/3 = 3.33333.. which is truncated to 3.

# Example 2:
# Input: dividend = 7, divisor = -3
# Output: -2
# Explanation: 7/-3 = -2.33333.. which is truncated to -2.

# Example 3:
# Input: dividend = 0, divisor = 1
# Output: 0

# Example 4:
# Input: dividend = 1, divisor = 1
# Output: 1
 

# Constraints:
# -2^31 <= dividend, divisor <= 2^31 - 1
# divisor != 0

tests = [
    {
        'dividend': 7,
        'divisor': 7,
        'output': 1,
    },
    {
        'dividend': 7,
        'divisor': 3,
        'output': 2,
    },
    {
        'dividend': -3,
        'divisor': -7,
        'output': 0,
    },
    {
        'dividend': -7,
        'divisor': 3,
        'output': -2,
    },
    {
        'dividend': -3,
        'divisor': 7,
        'output': 0,
    },
    {
        'dividend': 0,
        'divisor': 14,
        'output': 0,
    },
    {
        'dividend': 12,
        'divisor': 1,
        'output': 12,
    }
]

def do_division(dividend, divisor):
    q = 0

    if dividend == 0:
        return 0
    
    if divisor == 1:
        return dividend

    while dividend >= divisor:
        q += 1
        dividend -= divisor

    return q

def solution(dividend, divisor):
    mul = 1

    if dividend < 0:
        mul *= -1
        dividend *= -1
    
    if divisor < 0:
        mul *= -1
        divisor *= -1
    
    return (mul * do_division(dividend, divisor))

counter = 1
for test in tests:
    if test['output'] == solution(test['dividend'], test['divisor']):
        print(f"Test Case {counter} Passed!")
    else:
        print(f"Test Case {counter} Failed!")
        print(f"Dividend: {test['dividend']}")
        print(f"Divisor: {test['divisor']}") 
        print(f"Expected Output: {test['output']}")
        print(f"Obtained Output: {solution(test['dividend'], test['divisor'])}")
    
    print()
    counter += 1
