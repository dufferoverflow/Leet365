"""
Monotonic Array 
Write a function that takes in an array of integers and returns a boolean representing whether the array is monotonic.
An array is said to be monotonic if its elements, from left to right, are entirely non-increasing or entirely non-decreasing. 
Non-increasing elements aren't necessarily exclusively decreasing they simply don't increase. Similarly, non-decreasing elements aren't necessarily exclusively increasing; they simply don't decrease. 
Note that empty arrays and arrays of one element are monotonic. 
Sample Input array = (-1, -5, -10, -1100, -1100, -1101, -1102, -9001] 
Sample Output true



"""


def isMonotonic(array):
    # Write your code here.
   #i used array_new = array_old to copy arrays and this only does a shallow copy in python, careful! 
   #use array.copy() instead
   array_sort_dec = array.copy()
   array_sort_asc = array.copy()
   
   array_sort_dec.sort()
   array_sort_asc.sort(reverse=True)

   if array_sort_asc == array or array_sort_dec == array :
      return True
   return False
     
input = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
out = isMonotonic(input)
print(out)