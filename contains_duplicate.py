# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false

# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

# Constraints:
# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109

tests = [
    {
        'nums': [1,2,3,1],
        'output': True
    },
    {
        'nums': [1,2,3,4],
        'output': False
    },
    {
        'nums': [1,1,1,3,3,4,3,2,4,2],
        'output': True
    }
]

def solution(nums):
    hash_map = dict()

    for i in nums:
        if i in hash_map:
            return True
        else:
            hash_map[i] = 1
    
    return False

counter = 1
for test in tests:
    if test['output'] == solution(test['nums']):
        print(f"Test Case {counter} Passed!")
    else:
        print(f"Test Case {counter} Failed!")
    
    print()
    counter += 1