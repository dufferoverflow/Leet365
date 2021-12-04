# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Example 2:
# Input: strs = [""]
# Output: [[""]]

# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]
 
# Constraints:
# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.

# Simplification and algorithm:
# Two words are anagrams if and only if the count of a particular character in those words is the same
# Thus, we can maintain a dictionary where the count of the characters is the key and the list of words is the value
# Note that a list is non-hashable. Thus we need the key to be a tuple of 26 integer values, each corresponding to one alphabet 

# For example,
# strs = ["aab", "aba", "baa", "abbcc"]
# The dictionary we maintain will be as follows:
# {
#   (2, 1, 0, 0 ...., 0): ["aab", "aba", "baa", "abbcc"]
#   (1, 2, 2, 0, 0 ...., 0): ["abbcc"]
# }
# A list of the values of the dictionary is the list of anagrams

# 1. For each word, calculate the frequency of occurrence of each character
# 2. Check if the resulting tuple is present in the dictionary
# 3. If present, append word to the list
# 4. If not present, add count tuple to the dictionary and create a list with the word in it as the value

tests = [
    {
        "strs": ["eat","tea","tan","ate","nat","bat"],
        "output": [["bat"],["nat","tan"],["ate","eat","tea"]]
    },
    {
        "strs": [""],
        "output": [[""]]
    },
    {
        "strs": ["a"],
        "output": [["a"]]
    }
]

def solution(strs):
    word_dict = dict()    
    
    for word in strs:
        count = [0] * 26
        
        for alphabet in word:
            count[ord(alphabet) - ord('a')] += 1

        try:
            word_dict[tuple(count)].append(word)
        except KeyError:
            word_dict[tuple(count)] = [word] 
    
    return word_dict.values()

counter = 1
for test in tests:
    print("Test Case " + str(counter))
    print("Input: " + str(test["strs"]))
    print("Expected Output: " + str(test["output"]))
    print("Obtained Output: " + str(solution(test["strs"])))
    print()

