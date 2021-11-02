enum state { wall, passage, start, end, visited };

typedef struct tile {
  enum state state;
  void (*get_state)(struct tile *);
} tile;

typedef struct maze {
  tile **grid;
  void (*clear)(struct maze *);
} maze;

maze new_maze()
