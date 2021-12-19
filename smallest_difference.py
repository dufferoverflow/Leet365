"""
Smallest Difference Write a function that takes in two non-empty arrays of integers, finds the pair of numbers (one from each array) whose absolute difference is closest to zero, and returns an array containing these two numbers, with the number from the first array in the firs position. 
Note that the absolute difference of two integers is the distance between them on the real number line. 
For example, the absol difference of -5 and 5 is 10, and the absolute difference of -5 and -4 is 1. 
You can assume that there will only be one pair of numbers with the smallest difference. 
Sample Input arrayOne = (-1, 5, 10, 20, 28, 3] 
arrayTwo = [26, 134, 135, 15, 17) 
Sample Output [ 28, 26)

"""


def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    zero_diff = float('inf')    
    out = [] 
	
    for i in range(len(arrayOne)):
        for j in range(len(arrayTwo)):
            zero_diff_curr =abs(0 - abs(arrayOne[i]-arrayTwo[j]))
            if zero_diff_curr < zero_diff:
                zero_diff = zero_diff_curr
                i_l = arrayOne[i] 
                j_l = arrayTwo[j]
			
    out.append(i_l)
    out.append(j_l)
    return out

arrayOne = [-1, 5, 10, 20, 28, 3] 
arrayTwo = [26, 134, 135, 15, 17]
ans = smallestDifference(arrayOne, arrayTwo)
print(ans)
