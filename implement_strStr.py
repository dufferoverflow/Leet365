# from typing import type_check_only


# Implement strStr().

# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Clarification:

# What should we return when needle is an empty string? This is a great question to ask during an interview.

# For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

# Example 1: Length of haystack is greater than needle
# haystack = photosynthesis
# needle = mango 
# output = -1

# Example 2: Length of haystack is smaller than needle
# haystack = the
# needle = photosynthesis
# output = -1

# Example 3: Needle does not exist
# haystack = darthvader
# needle = yoda
# output = -1

# Example 4: Needle does exist
# haystack = photosynthesis
# needle = the
# output = 7

# Example 5: Needle is empty
# haystack = photosynthesis
# needle = ""
# output = 0

# Example 6: Haystack is empty
# haystack = ""
# needle = panda
# output = -1

# Constraints:
# 0 <= haystack.length, needle.length <= 5 * 104
# haystack and needle consist of only lower-case English characters.

tests = [
    {
        # Length of haystack is greater than needle
        'haystack': "photosynthesis",
        'needle': "mango",
        'output': -1
    },
    {
        # Length of haystack is smaller than needle
        'haystack': "the",
        'needle': "photosynthesis",
        'output': -1
    },
    {
        # Needle does not exist
        'haystack': "darthvader",
        'needle': "yoda",
        'output': -1
    },
    {
        # Needle does exist
        'haystack': "photosynthesis",
        'needle': "the",
        'output': 8
    },
    {
        # Needle is empty
        'haystack': "photosynthesis",
        'needle': "",
        'output': 0
    },
    {
        # Haystack is empty
        'haystack': "",
        'needle': "panda",
        'output': -1
    }
]

def solution_n(haystack, needle):
    lenh  = len(haystack)
    lenn = len(needle)
    i = 0

    if(lenh < lenn):
        return -1
    
    if lenn == 0:
        return 0

    if lenh == 0:
        return -1

    while i <= (lenh - lenn):
        substr = haystack[i:i+lenn]
        if substr == needle:
            return i
        i += 1

    return -1

counter  = 1
for test in tests:
    if test['output'] == solution_n(test['haystack'], test['needle']):
        print(f"Test Case {counter} Passed!")
    else:
        print(f"Test Case {counter} Failed!")
        print(f"Haystack: {test['haystack']}")
        print(f"Needle: {test['needle']}")
        print(f"Expected Output: {test['output']}")
        print(f"Obtained Output: {solution_n(test['haystack'], test['needle'])}")
    print()
    counter +=1
