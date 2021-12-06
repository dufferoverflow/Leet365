# We have n chips, where the position of the ith chip is position[i].

# We need to move all the chips to the same position. In one step, we can change the position of the ith chip from position[i] to:

#     position[i] + 2 or position[i] - 2 with cost = 0.
#     position[i] + 1 or position[i] - 1 with cost = 1.

# Return the minimum cost needed to move all the chips to the same position.

# Example 1
# Input: position = [1,2,3]
# Output: 1
# Explanation:
# Initial Setup:
#
# x     x       x
# 1     2       3 
#
# First step: Move the chip at position 3 to position 1 with cost = 0.
#
# x
# x     x 
# 1     2       3           Cost = 0
#
# Second step: Move the chip at position 2 to position 1 with cost = 1.
#
# x
# x
# x
# 1     2       3           Cost = 1
# Total cost is 1.

# Example 2
# Input: position = [2,2,2,3,3]
# Output: 2
# Explanation: We can move the two chips at position  3 to position 2. Each move has cost = 1. The total cost = 2.

#     x
#     x       x
#     x       x
# 1   2       3           Initial

#     x
#     x
#     x       
#     x       x
# 1   2       3           Cost = 1

#     x
#     x
#     x
#     x
#     x
# 1   2       3           Cost = 2

# Example 3:
# Input: position = [1,1000000000]
# Output: 1

# Constraints:

#     1 <= position.length <= 100
#     1 <= position[i] <= 10^9

# Explanation and Algorithm
# Jumping two positions is free. Jumping one position costs us a value of 1. This means that we can move all the odd position chips to position 1 (P1)
# and even position chips to position 2 (P2) without incurring any cost. Now we have two piles, one at P1 and other at P2. We can either 
# move the P1 pile to P2 or the P2 pile to P1. In both case, the cost will be the number of chips in the pile being moved. Since we need to minimize
# the cost, we must move the smaller pile

# 1. Count the number of odd positions
# 2. Count the number of even positions
# 3. Minimum of odd_count and even_count is the minimum cost

tests = [
    {
        'position': [1,2,3],
        'output': 1
    },
    {
        'position': [2,2,2,3,3],
        'output': 2
    },
    {
        'position': [1,1000000000],
        'output': 1
    }
]

def solution(position):
    odd_count = 0
    even_count = 0
    for pos in position:
        if pos % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    
    return min(odd_count, even_count)

counter = 1
for test in tests:
    if test['output'] == solution(test['position']):
        print(f"Test Case {counter} Passed!")
    else:
        print(f"Test Case {counter} Failed!")
        print(f"Position: {test['position']}")
        print(f"Expected Output: {test['output']}")
        print(f"Obtained Output: {solution(test['position'])}")
    print()
    counter += 1