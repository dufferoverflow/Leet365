# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Example 2:
# Input: nums = [1], k = 1
# Output: [1]

from collections import OrderedDict
def topKFrequent(nums, k):
    freq = OrderedDict()
    output = []
    for i in nums:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    
    for element, occr in sorted(freq.items(), key= lambda x: x[1], reverse=True):
        output.append(element)
    
    return output[:k]
