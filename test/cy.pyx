
class Square:
    def __init__(self, int x, int y, int length, int width):
        self.x = x;
        self.y = y;
        self.length = length;
        self.width = width;
        vx = 5;
    
    def move(self):
        if self.x > self.width or self.x < 0:
            self.x = -self.x;
        self.x += self.vx;

