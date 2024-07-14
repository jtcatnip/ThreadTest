import time


class Thread2:
    x = 1

    def __init__(self, name):
        self.num = 0
        self.name = name
        print("Thread2: ", self.name)

    def wait(self, num: object) -> object:
        print("Starting to sleep")
        time.sleep(self.num)
        print("Completed sleep")
