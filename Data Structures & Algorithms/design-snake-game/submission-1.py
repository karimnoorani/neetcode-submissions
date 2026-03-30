class SnakeGame:
    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.posQ = deque([(0, 0)])
        self.posSet = set([(0, 0)])
        self.width = width
        self.height = height
        self.food = food[::-1]
        self.score = 0

    def move(self, direction: str) -> int:
        r, c = self.posQ[-1]
        if direction == 'R':
            c += 1
        elif direction == 'U':
            r -= 1
        elif direction == 'D': 
            r += 1
        else:
            c -= 1
        
        if min(r, c) < 0 or r == self.height or c == self.width or (r, c) in self.posSet:
            return -1
        
        if self.food and [r, c] == self.food[-1]:
            self.score += 1
            self.food.pop()
        
        self.posQ.append((r, c))
        self.posSet.add((r, c))

        if len(self.posQ) > self.score + 1:
            r, c = self.posQ.popleft()
            self.posSet.remove((r, c))
        
        return self.score
# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
