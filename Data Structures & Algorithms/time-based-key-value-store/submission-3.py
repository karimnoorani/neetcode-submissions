class TimeMap:
    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if len(self.store[key]) == 0 or timestamp < self.store[key][0][0]:
            return ""
        
        lower, upper = 0, len(self.store[key])-1
        res = ""
        while lower <= upper:
            middle = (lower + upper) // 2

            if self.store[key][middle][0] <= timestamp:
                lower = middle + 1
                res = self.store[key][middle][1]
            else:
                upper = middle - 1
        
        return res