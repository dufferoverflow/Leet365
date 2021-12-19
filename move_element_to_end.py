"""
Move Element To End 
You're given an array of integers and an integer. 
Write a function that moves all instances of that integer in the array to the end of the array and returns the array. 
The function should perform this in place (i.e., it should mutate the input array) and doesn't need to maintain the order of the other integers. 

Sample Input array = [2, 1, 2, 2, 2, 3, 4, 2] 
toMove = 2 
Sample Output [1, 3, 4, 2, 2, 2, 2, 2] 
the numbers 1, 3, and 4 could be ordered differently
"""


def moveElementToEnd(array, toMove):
    # Write your code here.
    start = 0 
    end = len(array)-1
    while (start< end):
        if array[end]==toMove:
            end = end - 1 
        if array[start]==toMove and array[end]!= toMove:
            temp = array[start]
            array[start] = array[end]
            array[end] = temp 
            start = start +1 
            end = end -1 
        if array[start]!= toMove:
            start = start + 1 
    return array

array = [2, 1, 2, 2, 2, 3, 4, 2 ]
toMove = 2
ans = moveElementToEnd(array, toMove)
print(ans)

