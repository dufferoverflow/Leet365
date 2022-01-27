# Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

# A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

# Example 1:
# Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
# Output: true
# Explanation:
# In the above grid, the diagonals are:
# "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
# In each diagonal all elements are the same, so the answer is True.

# Example 2:
# Input: matrix = [[1,2],[2,2]]
# Output: false
# Explanation:
# The diagonal "[1, 2]" has different elements.
 
# Constraints:
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 20
# 0 <= matrix[i][j] <= 99

def solution(matrix):
    visited = dict()

    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[i])):
            if not (i,j) in visited:
                visited[(i,j)] = True
                
                # evaluating upper left
                if not (i-1 < 0 or j-1 < 0):
                    if matrix[i-1][j-1] != matrix[i][j]:
                        return False

                # evaluating bottom right
                if not (i+1 >= len(matrix) or j+1 >= len(matrix[i])):
                    visited[(i+1,j+1)] = True
                    if matrix[i+1][j+1] != matrix[i][j]:
                       return False
    
    return True