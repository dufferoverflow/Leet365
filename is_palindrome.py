#O(n) time and O(1) space
def isPalindrome(string):
    # Write your code here.
	last = len(string)
	check = 0 
	for i in range(len(string)):
		if string[i]==string[last-1]:
			last = last -1
		else :
			check = 1
			break
	if check ==0:
		return True
	else:
		return False
			
 
test = "abcdcba"
res = isPalindrome(test)
print(test)
print(res)
test_2 = "ab"
res_2 = isPalindrome(test_2)
print(test_2)
print(res_2)