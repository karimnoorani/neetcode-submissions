class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2map = defaultdict(list)
        for i, n in enumerate(nums2):
            nums2map[n].append(i)
        
        res = []
        for n in nums1:
            res.append(nums2map[n].pop())
        
        return res