# Given a string s which represents an expression, evaluate this expression and return its value. 

# The integer division should truncate toward zero.

# You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

# Example 1:
# Input: s = "3+2*2"
# Output: 7

# Example 2:
# Input: s = " 3/2 "
# Output: 1

# Example 3:
# Input: s = " 3+5 / 2 "
# Output: 5

def calculate(s):
    s = s.strip()
    if len(s) < 3:
        return s
    
    stack = []
    operation = "+"
    num = ""

    for i, c in enumerate(s):
        if c == ' ':
            continue
        
        if c.isnumeric():
            num += c
        
        if c in "+-*/" or i == len(s) - 1:
            if operation == "+":
                stack.append(int(num))
            elif operation == "-":
                stack.append(-int(num))
            elif operation == "*":
                stack[-1] = stack[-1] * int(num)
            elif operation == '/':
                stack[-1] = int(stack[-1] / int(num))
                    
            num = ""
            operation = c

    return sum(stack)