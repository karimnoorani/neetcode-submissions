class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        hand.sort()
        groups = {i:[] for i in range(len(hand)//groupSize)}

        def dfs(i):
            if i == len(hand):
                return True
            
            j = 0
            while len(groups[j]) == groupSize or (groups[j] and groups[j][-1] + 1 != hand[i]):
                j += 1
                if j >= len(groups):
                    return False
            
            groups[j].append(hand[i])
            return dfs(i+1)

        return dfs(0)