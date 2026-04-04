class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0
        j = 0

        while i < len(word) and j < len(abbr):
            num = 0
            while j < len(abbr) and abbr[j].isdigit():
                if abbr[j] == '0' and num == 0:
                    return False
                num = (num*10) + int(abbr[j])
                j += 1
            
            if num > 0:
                i += num
                continue
            
            if word[i] != abbr[j]:
                return False
            else:
                i += 1
                j += 1
        
        return i == len(word) and j == len(abbr)