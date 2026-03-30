class TimeMap:

    def __init__(self):
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        L, R = 0, len(self.data[key])-1
        
        while L <= R:
            M = (L+R)//2

            if self.data[key][M][0] > timestamp:
                R = M - 1
            else:
                res = self.data[key][M][1]
                L = M + 1
        
        return res

