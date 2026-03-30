class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        hand.sort()
        usedIndex = set()

        while len(usedIndex) != len(hand):
            currGroup = []
            for i in range(len(hand)):
                if len(currGroup) == groupSize:
                    break

                if i in usedIndex:
                    continue
                
                if currGroup and hand[i] == currGroup[-1]:
                    continue
                
                if currGroup and hand[i] != currGroup[-1]+1:
                    print(hand[i], currGroup)
                    return False

                usedIndex.add(i)
                currGroup.append(hand[i])
            
            if len(currGroup) != groupSize:
                return False
        
        return True