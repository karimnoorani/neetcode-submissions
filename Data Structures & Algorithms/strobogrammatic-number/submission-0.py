class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        stroDict = {"6": "9", "0": "0", "8": "8", "9": "6", "1": "1"}
        num2 = []

        for c in num:
            if c not in stroDict:
                return False
            num2.append(stroDict[c])
        
        return num == "".join(num2[::-1])