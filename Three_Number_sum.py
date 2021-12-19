""""
Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. 
The function should find all triplets in the array that sum up to the target sum and return a two-dimensional array of all these triplets. 
The numbers in each triplet should be ordered in ascending order, and the triplets themselves should be ordered in ascending order with respect to the numbers they hold.
If no three numbers sum up to the target sum, the function should return an empty array.

"""

#time O(n^2)
#space O(n)
def threeNumberSum(array, targetSum):
    # Write your code here.
    nums =[]
    array.sort()
    print("target", targetSum)
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            sum_2 = array[i]+array[j]
            third = targetSum - sum_2
            print(array[i], array[j], third)
            if third in array and third!= array[i] and third!=array[j] :
                temp = [array[i], array[j],third]
                temp.sort()
                #print(temp)
                if temp in nums:
                    break
                nums.append(temp)
				#print(nums.sort())
                continue
            else:
                continue
    nums_sorted = sorted(nums)
    return nums_sorted

array= [1, 2, 3, 4, 5, 6, 7, 8, 9, 15]
targetSum= 18
ans = threeNumberSum(array, targetSum)
print(ans)