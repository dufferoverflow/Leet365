# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:
# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.

tests = [
    {
        "nums": [2,7,11,15],
        "target": 9,
        "output": [0,1]
    },
    {
        "nums": [3,2,4],
        "target": 6,
        "output": [1,2]
    },
    {
        "nums": [3,3],
        "target": 6,
        "output": [0,1]
    }
]

def solution_nsquared(nums, target):
    output = list()

    for i in range(0,len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                output = [i,j]
                break

    return output

def solution_n(nums, target):
    # x + y = target
    # y = target - x
    # if we have come across y before, return [position_of_x, position_of_y]
    # if we have not come across y before, add x to a hash map
    
    output = list()
    hash_map = dict()

    for i in range(0, len(nums)):
        y = target - nums[i]
        try:
            hash_map[y]
            # y does exist in hash map, return [position_of_x, position_of_y]
            output = [hash_map[y], i]
            break            
        except KeyError:
            # y does not exist in hash map, add x to the hash map
            hash_map[nums[i]] = i
            
    return output


counter = 1
for test in tests:
    if test["output"] == solution_n(test["nums"], test["target"]):
        print("Test Case " + str(counter) + " Passed!")
    else:
        print("Test Case " + str(counter) + " Failed!")
        print("Input: " + str(test["nums"]))
        print("Target: " + str(test["target"]))
        print("Expected Output: " + str(test["output"]))
        print("Obtained Output: " + str(solution_n(test["nums"], test["target"])))
    print()
    counter += 1