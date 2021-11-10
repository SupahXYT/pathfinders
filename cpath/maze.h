#include "tile.h"

typedef struct maze {
  int width, height;
  tile grid[10][10];

  void (*clear)(struct maze *);
  void (*block)(struct maze *);
  void (*flush)(struct maze *);
  void (*print)(struct maze *);
  void (*gen_prim)(struct maze *);
  int *(*dfs)(struct maze *, int, int);
} maze;

void clear_maze(maze *);
void block_maze(maze *);
void flush_maze(maze *);
void print_maze(maze *);
void gen_prim_maze(maze *);

int *dfs_maze(maze *, int, int);
