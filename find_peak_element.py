# A peak element is an element that is strictly greater than its neighbors.

# Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

# You may imagine that nums[-1] = nums[n] = -∞.

# You must write an algorithm that runs in O(log n) time.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.

# Example 2:
# Input: nums = [1,2,1,3,5,6,4]
# Output: 5
# Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.

# Constraints:
# 1 <= nums.length <= 1000
# -231 <= nums[i] <= 231 - 1
# nums[i] != nums[i + 1] for all valid i.
import sys

def is_peak(pos, nums):
    curr = nums[pos]
    if pos == 0:
        prev = -sys.maxsize
        next = nums[pos+1]
    elif pos == len(nums) - 1:
        next = -sys.maxsize
        prev = nums[pos-1]    
    else:
        prev = nums[pos-1]
        next = nums[pos+1]
    
    if curr > prev and curr > next:
        return 0
    elif curr <= prev:
        return -1
    else:
        return 1

def solution(nums):
    if len(nums) == 1:
        return 0
    if len(nums) == 2:
        return nums.index(max(nums[0], nums[1]))
    
    left = 0
    right = len(nums) - 1

    while not left > right: 
        pos = (left + right) // 2
        if is_peak(pos, nums) == 0:
            return pos
        elif is_peak(pos, nums) == -1:
            right = pos - 1
        else:
            left = pos + 1
