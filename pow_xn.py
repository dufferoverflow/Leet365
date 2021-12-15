# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

# Example 1:
# Input: x = 2.00000, n = 10
# Output: 1024.00000

# Example 2:
# Input: x = 2.10000, n = 3
# Output: 9.26100

# Example 3:
# Input: x = 2.00000, n = -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25

# Constraints:
# -100.0 < x < 100.0
# -231 <= n <= 231-1
# -104 <= xn <= 104

# Algorithm:
# 1. If n is even, xⁿ = xⁿ/² * xⁿ/²
# 2. If n is odd, xⁿ = x * xⁿ⁻¹/² * xⁿ⁻¹/²

def myPow(x,n):
    if n == 0:
        return 1
    if n == 1:
        return x
    
    if n < 0:
        x = 1/x
        n *= -1
    
    if n%2 == 0:
        return myPow(x,n/2) * myPow(x,n/2)
    else:
        return x * myPow(x,(n-1)/2) * myPow(x,(n-1)/2)

