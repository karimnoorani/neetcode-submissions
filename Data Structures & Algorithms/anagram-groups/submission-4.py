class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1

            # if tuple(count) not in res:
            #     res[tuple(count)] = []

            res[tuple(count)].append(s)

        return res.values()