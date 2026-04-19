class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.numbers = set([i for i in range(maxNumbers)])

    def get(self) -> int:
        return self.numbers.pop() if len(self.numbers) > 0 else -1

    def check(self, number: int) -> bool:
        return number in self.numbers

    def release(self, number: int) -> None:
        self.numbers.add(number)


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
