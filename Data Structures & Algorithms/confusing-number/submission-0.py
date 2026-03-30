class Solution:
    def confusingNumber(self, n: int) -> bool:
        n = str(n)
        valid = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
        newNum = []
        for c in n:
            if c not in valid:
                return False
            
            newNum.append(valid[c])
            
        return "".join(newNum[::-1]) != n
