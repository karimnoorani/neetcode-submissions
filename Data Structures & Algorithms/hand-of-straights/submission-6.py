class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)
        heap = list(count.keys())
        heapq.heapify(heap)

        groups = 0

        while groups < len(hand)//groupSize:
            start = heap[0]

            for i in range(groupSize):
                if count.get(start+i, 0) == 0:
                    return False
                
                count[start+i] -= 1
                if count[start+i] == 0:
                    if heap[0] != start+i:
                        return False
                    heapq.heappop(heap)
            groups += 1
        
        return True