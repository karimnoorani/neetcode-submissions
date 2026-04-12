class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        usersToWebsites = defaultdict(list)
        patternScore = defaultdict(int)
        res = []

        for time, user, site in sorted(zip(timestamp, username, website)):
            usersToWebsites[user].append(site)

            if len(usersToWebsites[user]) >= 3:
                patternScore[tuple(usersToWebsites[user][-3:])] += 1
                
                score = patternScore[tuple(usersToWebsites[user][-3:])]
                maxScore = patternScore[tuple(res)]
                if score > maxScore or (score == maxScore and usersToWebsites[user][-3:] < res):
                    res = usersToWebsites[user][-3:]
        
        return res