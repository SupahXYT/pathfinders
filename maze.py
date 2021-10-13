import pygame

class maze:
    def __init__(self, width, height):
        self.maze = [[False for i in range(height)] for j in range(width)]


