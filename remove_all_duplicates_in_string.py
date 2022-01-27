# You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

# We repeatedly make duplicate removals on s until we no longer can.

# Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

# Example 1:
# Input: s = "abbaca"
# Output: "ca"
# Explanation: 
# For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".

# Example 2:
# Input: s = "azxxzy"
# Output: "ay"

# Constraints:
# 1 <= s.length <= 105
# s consists of lowercase English letters.

tests = [
    {
        's': "abbaca",
        'output': "ca"
    },
    {
        's': "azxxzy",
        'output': "ay"
    },
    {
        's': "",
        'output': ""
    },
    {
        's': "a",
        'output': "a"
    }
]

def solution(s):
    if len(s) < 2:
        return s
    else:
        stack = " " + s[0]
        for i in range(1, len(s)):
            if s[i] == stack[-1]:
                stack = stack[0:-1]
            else:
                stack += s[i]
    
    return stack.strip()

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