# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top? 

# Example 1:
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example 2:
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

# Constraints:
# 1 <= n <= 45

#Algorithm:
# This is basically the Fibonnaci series
# steps(n) = fibonacci(n+1)

tests = [
    {
        'n': 2,
        'output': 2
    },
    {
        'n': 3,
        'output': 3
    }
]

def solution(n):
    a = 1
    b = 1
    sum = 0
    for i in range(1,n):
        sum = a + b
        a = b
        b = sum
    return sum 

counter = 1
for test in tests:
    if test['output'] == solution(test['n']):
        print(f"Test Case {counter} Passed!")
    else:
        print(f"Test Case {counter} Failed!")
        print(f"Input: {test['n']}")
        print(f"Expected Output: {test['output']}")
        print(f"Obtained Output: {solution(test['n'])}")
    
    print()
    counter += 1