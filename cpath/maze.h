#include "tile.h"

typedef struct maze {
  int width, height;
  tile grid[10][10];
  tile *row;

  void (*clear)(void);
  void (*block)(void);
  void (*flush)(void);
  void (*draw)(void);
  void (*gen_prim)(void);
  void (*dfs)(int, int);
  void (*dfs_visual)(int, int);
} maze;
