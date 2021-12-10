# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

# Example 4:
# Input: s = "([)]"
# Output: false

# Example 5:
# Input: s = "{[]}"
# Output: true

# Constraints:
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

tests = [
    {
        's': "()",
        'output': True
    },
    {
        's': "()[]{}",
        'output': True
    },
    {
        's': "(]",
        'output': False
    },
    {
        's': "([)]",
        'output': False
    },
    {
        's': "{[]}",
        'output': True
    },
    {
        's': '[',
        'output': False
    }
]

stack = []

def push(x):
    stack.append(x)
    
def pop():
    global stack

    # Check if stack is empty
    if len(stack) == 0:
        return -1
    
    x = stack[-1]
    stack = stack[0:-1]
    return x

def solution_n(s):
    global stack
    stack = []
    paran_map = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for i in range(0, len(s)):
        if s[i] == '(' or s[i] == '{' or s[i] == '[':
            push(s[i])
        else:
            x = pop()
            if not paran_map[s[i]] == x:
                return False
    
    # If stack is not empty by the end of the string, then parantheses are not valid
    if not len(stack) == 0:
        return False
    
    return True

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

