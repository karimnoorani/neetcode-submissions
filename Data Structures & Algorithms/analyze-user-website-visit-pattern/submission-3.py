class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        usersToWebsites = defaultdict(list)
        patternScore = defaultdict(set)
        res = []

        for time, user, site in sorted(zip(timestamp, username, website)):
            usersToWebsites[user].append(site)

            if len(usersToWebsites[user]) >= 3:
                for i in range(len(usersToWebsites[user])-2):
                    for j in range(i+1, len(usersToWebsites[user])-1):
                        pattern = [usersToWebsites[user][i], usersToWebsites[user][j], site]
                        patternScore[tuple(pattern)].add(user)
                        score = len(patternScore[tuple(pattern)])
                        maxScore = len(patternScore[tuple(res)])

                        if score > maxScore or (score == maxScore and pattern < res):
                            res = pattern
        
        return res