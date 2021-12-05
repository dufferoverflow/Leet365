# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# Example 1:
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Example 2:
# Input: list1 = [], list2 = []
# Output: []

# Example 3:
# Input: list1 = [], list2 = [0]
# Output: [0]

# Constraints:
# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.

tests = [
    {
        "list1": [1,2,4], 
        "list2": [1,3,4],
        "output": [1,1,2,3,4,4]
    },
    {
        "list1": [], 
        "list2": [0],
        "output": [0]
    }
]

def solution_n(list1, list2):
    output = []

    l1 = 0
    l2 = 0

    while l1 < len(list1) and l2 < len(list2):
        if list1[l1] < list2[l2]:
            output.append(list1[l1])
            l1 += 1
        else:
            output.append(list2[l2])
            l2 += 1
    
    if l1 == len(list1):
        output.append(*list2[l2:])
    else:
        output.append(*list1[l1:])

    return output

counter = 0
for test in tests:
    if test['output'] == solution_n(test['list1'], test['list2']):
        print(f"Test Case {counter} Passed!")
    else:
        print(f"Test Case {counter} Failed!")
        print(f"List 1: {test['list1']}")
        print(f"List 2: {test['list2']}")
        print(f"Expected Output: {test['output']}")
        print(f"Obtained Output: {solution_n(test['list1'], test['list2'])}")
    print()
    counter += 1