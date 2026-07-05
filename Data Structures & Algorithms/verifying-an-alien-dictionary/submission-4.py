class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        letter_to_index = {char: index for index, char in enumerate(order)}

        for index in range(len(words)-1):
            word1 = words[index]
            word2 = words[index+1]
            verified = False

            for char_index in range(min(len(word1), len(word2))):
                if letter_to_index[word1[char_index]] < letter_to_index[word2[char_index]]:
                    verified = True
                    break
                
                if letter_to_index[word1[char_index]] > letter_to_index[word2[char_index]]:
                    return False
            
            if not verified and len(word1) > len(word2):
                return False
        
        return True