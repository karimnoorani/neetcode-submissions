class Solution:
    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:
        keyMapping = {key: value for key, value in replacements}
        cache = {}

        def resolve(text):
            if text in cache:
                return cache[text]

            substituted_string = []
            for substring in text.split('%'):
                if substring in keyMapping:
                    substituted_string.append(resolve(keyMapping[substring]))
                else:
                    substituted_string.append(substring)
            
            cache[text] = "".join(substituted_string)
            return cache[text]

        for key in keyMapping:
            keyMapping[key] = resolve(key)

        return resolve(text)