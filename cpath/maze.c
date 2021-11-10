#include "maze.h"
#include <stdio.h>

char gettc(tile *this) {
  switch (this->state) {
  case wall:
    return '#';
  case passage:
    return ' ';
  case visited:
    return 'S';
  default:
    return '@';
  }
}

void clear_maze(maze *this) {
  for (int i = 0; i < this->width; i++) {
    for (int j = 0; j < this->width; j++) {
      this->grid[i][j].state = passage;
    }
  }
}

void block_maze(maze *this) {
  for (int i = 0; i < this->width; i++) {
    for (int j = 0; j < this->width; j++) {
      this->grid[i][j].state = wall;
    }
  }
}

void flush_maze(maze *this) {
  for (int i = 0; i < this->width; i++) {
    for (int j = 0; j < this->width; j++) {
      if (this->grid[i][j].state == visited) {
        this->grid[i][j].state = passage;
      }
    }
  }
}

void print_maze(maze *this) {
  for (int i = 0; i < this->width; i++) {
    for (int j = 0; j < this->width; j++) {
      putchar(gettc(&(this->grid[i][j])));
    }
    putchar('\n');
  }
}

void gen_prim_maze(maze *this) {}

maze new_maze(void) {
  maze new;
  new.width = 10;
  new.height = 10;

  for (int i = 0; i < new.width; i++) {
    for (int j = 0; j < new.height; j++) {
      new.grid[i][j].state = wall;
    }
  }

  new.print = print_maze;
  return new;
}

int main(void) {
  maze m = new_maze();
  m.grid[2][4].state = passage;
  m.print(&m);
}
