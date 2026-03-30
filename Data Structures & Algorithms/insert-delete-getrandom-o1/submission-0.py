class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.numsMap = {}

    def insert(self, val: int) -> bool:
        if val in self.numsMap:
            return False
        self.numsMap[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.numsMap:
            return False
        valIndex = self.numsMap[val]
        self.nums[valIndex], self.nums[len(self.nums)-1] = self.nums[len(self.nums)-1], self.nums[valIndex]
        
        self.numsMap[self.nums[valIndex]] = valIndex
        self.nums.pop()
        del self.numsMap[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()