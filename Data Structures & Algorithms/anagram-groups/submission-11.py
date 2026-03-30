class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        charMap = defaultdict(list)
        for s in strs:
            key = [0 for _ in range(26)]
            for c in s:
                i = ord(c) - ord('a')
                key[i] += 1
            charMap[tuple(key)].append(s)
        return list(charMap.values())