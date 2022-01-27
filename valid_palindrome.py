# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Example 2:
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

# Example 3:
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.

# Constraints:
# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.

def solution(s):
    s = s.strip()
    if len(s) == 0:
        return True
    
    sp = 0
    lp = len(s) - 1

    while not sp > lp:
        if s[sp].isalnum() and s[lp].isalnum():
            if not s[sp].lower() == s[lp].lower():
                return False
            sp += 1
            lp -= 1
        else:
            if not s[sp].isalnum():
                sp += 1
            if not s[lp].isalnum():
                lp -= 1
    
    return True


        
