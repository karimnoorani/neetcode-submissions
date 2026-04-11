class Solution:
    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:
        mappings = {f'%{key}%': val for key, val in replacements}
        text = text.split('_')
        for i in range(len(text)):
            while '%' in text[i]:
                t = text[i]
                key = t[t.index('%'):t.index('%')+3]
                text[i] = t.replace(key, mappings[key])
        return "_".join(text)