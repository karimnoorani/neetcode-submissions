class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def dfs(i, j):
            if j == len(s):
                if self.isPalindrome(s[i:j]):
                    res.append(path + [s[i:j]])
                return
            
            if self.isPalindrome(s[i:j]):
                path.append(s[i:j])
                dfs(j, j+1)
                path.pop()
            
            dfs(i, j+1)
        
        dfs(0, 1)
        return res


    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1

        while l <= r:
            if s[l] != s[r]:
                return False
            
            l += 1
            r -= 1
        
        return True