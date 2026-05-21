from itertools import combinations

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        usersToWebsites = defaultdict(list)
        patternToUsers = defaultdict(set)

        for time, user, website in sorted(zip(timestamp, username, website)):
            usersToWebsites[user].append(website)

        for user in usersToWebsites:
            for subseq in combinations(usersToWebsites[user], 3):
                patternToUsers[tuple(subseq)].add(user)
        
        patternHighestScore = tuple([])
        patternScore = 0
        for pattern in patternToUsers:
            if len(patternToUsers[pattern]) > patternScore or (len(patternToUsers[pattern]) == patternScore and pattern < patternHighestScore):
                patternHighestScore = pattern
                patternScore = len(patternToUsers[pattern])
        
        return list(patternHighestScore)