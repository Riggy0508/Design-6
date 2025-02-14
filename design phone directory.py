class PhoneDirectory:

    def __init__(self, maxNumbers: int):

        self.numbers={i for i in range(maxNumbers)}
        #print(self.numbers)

    def get(self) -> int:
        if not self.numbers:
            return -1
        else:
            return self.numbers.pop()
        

    def check(self, number: int) -> bool:
        if number in self.numbers:
            return True
        else:
            return False

    def release(self, number: int) -> None:
        self.numbers.add(number)
        