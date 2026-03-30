class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        currBills = {5: 0, 10: 0}

        for b in bills:
            if b == 5:
                currBills[5] += 1
            elif b == 10:
                if currBills[5] == 0:
                    return False
                currBills[5] -= 1
                currBills[10] += 1
            else:
                if currBills[10] == 0:
                    if currBills[5] < 3:
                        return False
                    else:
                        currBills[5] -= 3
                else:
                    if currBills[5] == 0:
                        return False
                    currBills[10] -= 1
                    currBills[5] -= 1
        
        return True
                