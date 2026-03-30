class Logger:
    def __init__(self):
        self.timeMap = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if timestamp >= self.timeMap.get(message, 0):
            self.timeMap[message] = timestamp + 10
            return True
        return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
