from typing import List

def generate_parentheses(n: int) -> List[str]:
    ans = []
    def dfs(path, idx, openC, closeC):
        if idx == 2*n:
            ans.append(''.join(path))
        if openC < n:
            dfs(path+['('], idx+1, openC+1, closeC)
        if closeC < openC:
            dfs(path + [')'], idx+1, openC, closeC+1)
    dfs([], 0, 0, 0)
    return ans

if __name__ == '__main__':
    n = int(input())
    res = generate_parentheses(n)
    for line in sorted(res):
        print(line)

'''
Probably the most difficult part to me was to draw the tree, I actually 
had to look at the solution cause I wasn't able to really figure it out.
Once the tree was there, it is easy to figure out the cases, and then 
the solution showd that looping over the edges will not always be needed,
in this example we only needed open or close parentheses, so only two if
statements would do the trick.
'''