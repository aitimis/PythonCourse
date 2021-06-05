class MyNumber(int):
    def __init__(self, number):
        self.number = number

    def __iter__(self):
        return MyNumberIter(self.number)

class MyNumberIter:

    def __init__(self, number1):
        self.number_list = [i for i in range(1, number1 + 1)]
        # self.number = number1

    def __iter__(self):
        return self

    def __next__(self):
        if not self.number_list:
            raise StopIteration
        return self.number_list.pop(0)


m = MyNumber(7)

for i in m:
    print(i)

n = m + 1

for i in n:
    print(i)