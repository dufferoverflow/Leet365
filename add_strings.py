# Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

# You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

# Example 1:
# Input: num1 = "11", num2 = "123"
# Output: "134"

# Example 2:
# Input: num1 = "456", num2 = "77"
# Output: "533"

# Example 3:
# Input: num1 = "0", num2 = "0"
# Output: "0"

# Constraints:
# 1 <= num1.length, num2.length <= 104
# num1 and num2 consist of only digits.
# num1 and num2 don't have any leading zeros except for the zero itself.

def solution(num1, num2):
    # reverse string
    num1 = num1[::-1]
    num2 = num2[::-1]
    
    #normalise string
    ln1 = len(num1)
    ln2 = len(num2)
    if ln1 < ln2:
        num1 = num1 + '0'*(ln2-ln1)
    else:
        num2 = num2 + '0'*(ln1-ln2)
    
    carry = 0
    sum_string = ""
    for i in range(0,max(ln1,ln2)):
        sum = carry + ord(num1[i]) + ord(num2[i]) - 2*ord('0')
        if sum > 9:
            carry = 1
        else:
            carry = 0
        sum_string += str(sum%10)
    
    sum_string = sum_string[::-1]
    if carry == 1:
        sum_string = '1' + sum_string
    return sum_string