#include "maze.h"
#include <stdio.h>

maze new_maze(int width, int height) {
  maze new;
  new.width = width;
  new.height = height;

  for (int i = 0; i < width; i++) {
    for (int j = 0; j < height; j++) {
      new.grid[i][j].state = wall;
    }
  }

  return new;
}

void draw(maze *self) {
  for (int i = 0; i < self->height; i++) {
    for (int j = 0; j < self->width; j++) {
      putchar(self->grid[i][j].rep);
    }
    putchar('\n');
  }
}

int main(void) { /* maze m = new_maze(10, 10); */
}
