class Solution:
    def encode(self, strs: List[str]) -> str:
        result = []
        
        for word in strs:
            result.append(str(len(word))+"|"+word)
        
        return "".join(result)

    def decode(self, s: str) -> List[str]:
        result = []
        index = 0

        while index < len(s):
            length = 0
            
            while s[index] != "|":
                length = length*10 + int(s[index])
                index += 1
            
            index += 1 # skipping |

            result.append(s[index:index+length])
            index += length
        
        return result