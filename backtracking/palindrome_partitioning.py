from typing import List

def partition(s: str) -> List[List[str]]:
    '''
    Input: aab
    Output: 
    a a b
    aa b

    '''
    res = []
    n = len(s)
    def dfs(path: list, start):
        if start == n: # We agree we need to stop when we have reached the size of the string
            res.append(path)
        for i in range(start+1, n+1):
            prefix = s[start:i] # i represents the length of the prefix
            # For example in aab, with start = 0 and i = 2, prefix = aa
            if prefix == prefix[::-1]: # Validate prefix is a palindrome
                # send prefix found plus the end point of the prefix which will be the new starting point
                dfs(path+[prefix], i) 
    dfs([],0)
    return res

# Especial note: WHen passing lists to another list, make sure you are sending copies, otherwise you could be sending
# the same list over and over, and for example in the code above, you would delete all values of 'path' which let's
# say you have been passing to 'res', so the end result would be a pointer to the same list which would be empty
# Those lists should be different, you can use the .copy() method of list, or do a google search for other methods
# like the one used in the code.

if __name__ == '__main__':
    s = input()
    res = partition(s)
    for row in res:
        print(' '.join(row))