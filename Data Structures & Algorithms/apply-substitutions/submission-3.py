class Solution:
    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:
        keyMap = {}
        
        for key, value in replacements:
            keyMap["%" + key + "%"] = value
        
        substituted_text = []

        for key in text.split('_'):
            while '%' in key:
                index = key.find('%')
                key = key.replace(key[index:index+3], keyMap[key[index:index+3]])
            substituted_text.append(key)
        
        return "_".join(substituted_text)