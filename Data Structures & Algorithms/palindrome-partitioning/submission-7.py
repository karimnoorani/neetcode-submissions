class Solution:
    def partition(self, s: str) -> List[List[str]]:
        cache = {}
        
        def isPalindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        def dfs(index):
            if index == len(s):
                return [[]]
            
            if index in cache:
                return cache[index]
            
            result = []
            for end in range(index+1, len(s)+1):
                if isPalindrome(index, end-1):
                    for rest in dfs(end):
                        result.append([s[index:end]] + rest)
            cache[index] = result
            return cache[index]
        
        return dfs(0)