class Solution:
    def candy(self, ratings: List[int]) -> int:
        ratings = [float('-INF')] + ratings + [float('-INF')]
        candies = [0 if i in [0, len(ratings)-1] else 1 for i in range(len(ratings))]

        for i in range(1, len(candies)-1):
            if ratings[i] > ratings[i-1] and candies[i] <= candies[i-1]:
                candies[i] = candies[i-1] + 1
        
        for i in range(len(candies)-2, 0, -1):
            if ratings[i] > ratings[i+1] and candies[i] <= candies[i+1]:
                candies[i] = candies[i+1] + 1
        
        return sum(candies[1:-1])