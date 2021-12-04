# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity. 

# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

# Example 2:
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]

# Example 3:
# Input: nums = [], target = 0
# Output: [-1,-1]

# Constraints:
# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109
# nums is a non-decreasing array.
# -109 <= target <= 109

tests = [
    {
        #Element occurs twice in the list
        "nums": [5,7,7,8,8,10],
        "target": 8,
        "output": [3,4]
    },
    {
        #Element occurs only once in the list
        "nums": [5,7,7,8,8,10],
        "target": 10,
        "output": [5,5]
    },
    {
        #Element does not occur in the list
        "nums": [5,7,7,8,8,10],
        "target": 6,
        "output": [-1,-1]
    },
    #List is empty
    {
        "nums": [],
        "target": 8,
        "output": [-1,-1]
    }
]

def solution_n(nums, target):
    output = [-1,-1]
    
    for i in range(0, len(nums)):
        if nums[i] > target:
            break
        
        if nums[i] == target:
            #Match found. Check if this is first occurence
            if output[0] == -1:
                #Yes this is first occurrence
                output[0] = i
                output[1] = i
            else:
                #No, this is not the first occurence
                output[1] = i

    return output

counter = 1
for test in tests:
    if test["output"] == solution_n(test["nums"], test["target"]):
        print("Test Case " + str(counter) + " Passed!")
    else:
        print("Test Case "+ str(counter) + " Failed!")
        print("Array: " + str(test["nums"]))
        print("Target: " + str(test["target"]))
        print("Expected Output: " + str(test["output"]))
        print("Obtained Output: " + str(solution_n(test["nums"], test["target"])))
    print()
    counter += 1