class Logger:
    def __init__(self):
        self.timeMap = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.timeMap or timestamp >= self.timeMap[message]:
            self.timeMap[message] = timestamp + 10
            return True
        return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
