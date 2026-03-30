class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        adjList = {}
        emailToName = {}
        for account in accounts:
            for i in range(1, len(account)):
                if account[i] not in adjList:
                    adjList[account[i]] = []
                emailToName[account[i]] = account[0]
                for j in range(i+1, len(account)):
                    if account[j] not in adjList:
                        adjList[account[j]] = []
                    
                    adjList[account[i]].append(account[j])
                    adjList[account[j]].append(account[i])

                    emailToName[account[j]] = account[0]
        
        visited = set()
        print(adjList)
        def dfs(email, assocEmails):
            assocEmails.append(email)
            visited.add(email)

            for neighbor in adjList[email]:
                if neighbor not in assocEmails:
                    dfs(neighbor, assocEmails)
        
        res = []
        for email in adjList:
            if email not in visited:
                assocEmails = []
                dfs(email, assocEmails)
                res.append([emailToName[email]] + sorted(assocEmails))
        
        return res
        
        
