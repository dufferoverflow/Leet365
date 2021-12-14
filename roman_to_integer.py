# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

# Example 1:
# Input: s = "III"
# Output: 3

# Example 2:
# Input: s = "IV"
# Output: 4

# Example 3:
# Input: s = "IX"
# Output: 9

# Example 4:
# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.

# Example 5:
# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

# Example 6:
# Input: s = "L"
# Output: 50

# Constraints:
# 1 <= s.length <= 15
# s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
# It is guaranteed that s is a valid roman numeral in the range [1, 3999].

# Algorithm:
# 1. Start parsing the string from backwards
# 2. If the integer value of a roman character is less than the one after it, it needs to be subtracted
# 3. If the integer value of a roman character is not less than the one after it, it needs to be added
# Example - IV and VI
# I < V so we need to subtract I
# V > I so we need to add V
# 4. Edge Case: If input string has length 1, directly return the integer value

tests = [
    {
        's': "III",
        'output': 3
    },
    {
        's': "IV",
        'output': 4
    },
    {
        's': "IX",
        'output': 9
    },
    {
        's': "LVIII",
        'output': 58
    },
    {
        's': "MCMXCIV",
        'output': 1994
    },
    {
        's': "L",
        'output': 50
    }
]

def get_integer(roman):
    mapping = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    return mapping[roman]

def solution_n(s):

    if len(s) == 1:
        return get_integer(s)

    last = get_integer(s[-1])
    value = last
    i = len(s) - 2

    while i >= 0:
        curr = get_integer(s[i])
        if curr < last:
            value -= curr
        else:
            value += curr

        last = curr
        i -= 1
    
    return value


counter = 1
for test in tests:
    if test['output'] == solution_n(test['s']):
        print(f"Test Case {counter} Passed!")
    else:
        print(f"Test Case {counter} Failed!")
        print(f"Input: {test['s']}")
        print(f"Expected Output: {test['output']}")
        print(f"Obtained Output: {solution_n(test['s'])}")
    
    print()
    counter += 1

