enum state { wall, passage, start, dest, visited };

typedef struct tile {
  enum state state;
  int adj[2];
} tile;
