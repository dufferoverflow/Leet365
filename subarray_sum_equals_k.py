# Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

# Example 1:
# Input: nums = [1,1,1], k = 2
# Output: 2

# Example 2:
# Input: nums = [1,2,3], k = 3
# Output: 2

# Constraints:
# 1 <= nums.length <= 2 * 104
# -1000 <= nums[i] <= 1000
# -107 <= k <= 107

# References:
# https://www.youtube.com/watch?v=20v8zSo2v18
# https://www.youtube.com/watch?v=HbbYPQc-Oo4

def solution(nums, k):
    prefix_sum = 0
    hash_map = dict()
    counter = 0

    for i in nums:
        prefix_sum += i
        if prefix_sum == k:
            counter += 1
        if (prefix_sum - k) in hash_map:
            counter += hash_map[prefix_sum - k]
        if prefix_sum in hash_map:
            hash_map[prefix_sum] += 1
        else:
            hash_map[prefix_sum] = 1
        
        return counter

