import time


class Thread2:

    def __init__(self, name):
        self.num = 0
        self.name = name
        print("Thread2: ", self.name)

    def wait(self, num):
        print("Starting to sleep")
        time.sleep(self.num)
        print("Completed sleep")