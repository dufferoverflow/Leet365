# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

# Example 2:
# Input: nums = []
# Output: []

# Example 3:
# Input: nums = [0]
# Output: []

# Constraints:
# 0 <= nums.length <= 3000
# -10^5 <= nums[i] <= 10^5

def solution(nums):
    output = []
    if len(nums) < 3:
        return output
    
    nums = sorted(nums)
    prev_a = sys.maxsize
    for i, a in enumerate(nums):
        if i > 0 and nums[i - 1] == a:
            continue
        
        left = i + 1
        right = len(nums) - 1

        while left < right:
            three_sum = a + nums[left] + nums[right]
            if three_sum > 0:
                right -= 1
            elif three_sum < 0:
                left += 1
            else:
                output.append([a,nums[left],nums[right]])
                left += 1
                while nums[left] == nums[left - 1] and left < right:
                    left += 1
    return output