class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        window = len(cardPoints)-k
        res = total = sum(cardPoints)
        curSum = 0

        for i in range(len(cardPoints)):
            curSum += cardPoints[i]

            if i >= window:
                curSum -= cardPoints[i-window]
            
            if i >= window - 1:
                res = min(res, curSum)
        
        return total-res
