class Thread1:

    def __init__(self, name):
        self.sum = 0
        self.name = name
        print("name: ", name)

    def add(self, num1, num2):
        self.sum = 0
        self.sum = num1 + num2
        return self.sum

    def sub(self, num1, num2):
        self.sum = 0
        self.sum = num2 - num1
        return self.sum


