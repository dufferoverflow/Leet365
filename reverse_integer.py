# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# Example 1:
# Input: x = 123
# Output: 321

# Example 2:
# Input: x = -123
# Output: -321

# Example 3:
# Input: x = 120
# Output: 21

# Constraints:
# -2^31 <= x <= 2^31 - 1

def solution(x):
    MIN = -2 ** 31
    MAX  = (2 ** 31) - 1
    rev = 0
    divider = 10

    if x < 0:
        negative_multiplier = -1
        x = x * -1
    else:
        negative_multiplier = 1

    while x > 0:
        digit =  x % 10
        rev = (rev * 10) + digit
        x = x // 10
    
    rev *= negative_multiplier

    if rev < MIN:
        return 0
    if rev > MAX:
        return 0
        
    return rev 