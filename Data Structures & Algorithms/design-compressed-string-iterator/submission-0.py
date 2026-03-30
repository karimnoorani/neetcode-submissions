class StringIterator:
    def __init__(self, compressedString: str):
        self.q = deque()
        i = 0

        while i < len(compressedString):
            c = compressedString[i]
            i += 1
            freq = 0
            while i < len(compressedString) and compressedString[i].isdecimal():
                freq = freq * 10 + int(compressedString[i])
                i += 1
            self.q.append([c, freq])


    def next(self) -> str:
        if not self.q:
            return ''
        
        c = self.q[0][0]
        self.q[0][1] -= 1
        
        if self.q[0][1] == 0:
            self.q.popleft()
        
        return c

    def hasNext(self) -> bool:
        return len(self.q) > 0


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
