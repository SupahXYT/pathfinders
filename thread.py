import threading
from random import random 
from time import sleep

class Useful:
    def __init__(self):
        self.list = []

    def random(self):
        for i in range(15):
            self.list.append(random())
            sleep(1)

class Visualize:
    def __init__(self):
        self.use = Useful()

    def main(self):
        # upon request, start defs
        # then draw in main loop, only updating according to rects in maze
        t1 = threading.Thread(target=self.use.random)
        t1.start()
        while(True):
            self.print()
            sleep(1)

    # 'draw' function
    def print(self):
        while(len(self.use.list) > 0):
            element = self.use.list.pop(0)
            print(element)

if __name__ == '__main__':
    v = Visualize()
    v.main()
