class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = ""
        for i in range(len(num)-2):
            if num[i:i+3] in ["000", "111", "222", "333", "444", "555", "666", "777", "888", "999"]:
                if res == "" or int(num[i:i+3]) > int(res):
                    res = num[i:i+3]
        return res