class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        R = deque()
        D = deque()

        for i, c in enumerate(senate):
            if c == "R":
                R.append(i)
            else:
                D.append(i)
        
        while R and D:
            print(R, D)
            senatorR = R.popleft()
            senatorD = D.popleft()

            if senatorR < senatorD:
                R.append(senatorR+len(senate))
            else:
                D.append(senatorD+len(senate))
        
        return "Radiant" if len(R) > 0 else "Dire"


