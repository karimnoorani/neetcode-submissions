class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        heapq.heapify(boxes)
        stack = []
        prefix_min = float('inf')
        for space in warehouse:
            prefix_min = min(prefix_min, space)
            stack.append(prefix_min)
        res = 0
        
        while boxes:
            while stack and boxes[0] > stack[-1]:
                stack.pop()
            
            if not stack:
                break
            
            heapq.heappop(boxes)
            stack.pop()
            res += 1
        
        return res