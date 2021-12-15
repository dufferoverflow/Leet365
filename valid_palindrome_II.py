# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

# Example 1:
# Input: s = "aba"
# Output: true

# Example 2:
# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.

# Example 3:
# Input: s = "abc"
# Output: false

# Constraints:
# 1 <= s.length <= 105
# s consists of lowercase English letters.

tests = [
    {
        's': "aba",
        'output': True
    },
    {
        's': "abca",
        'output': True
    },
    {
        's': "abc",
        'output': False
    }
]

def solution(s):
    # Check if already palindrome
    if s == s[::-1]:
        return True
    
    left = 0
    right = len(s) - 1

    while not left > right:
        if not s[left] == s[right]:
            without_left = s[:left] + s[left+1:]
            without_right = s[:right] + s[right+1:]
            if without_left == without_left[::-1] or without_right == without_right[::-1]:
                return True
            else:
                return False
        
        left += 1
        right -= 1
    
    return False

counter = 1
for test in tests:
    if test['output'] == solution(test['s']):
        print(f"Test Case {counter} Passed!")
    else:
        print(f"Test Case {counter} Failed!")
        print(f"Input: {test['s']}")
        print(f"Expected Output: {test['output']}")
        print(f"Obtained Output: {solution(test['s'])}")
    
    print()
    counter += 1