enum state { wall, passage, start, dest, visited };

typedef struct tile {
  char rep;
  enum state state;
  struct tile *adj;

  void (*set_state)(struct tile *, enum state);
} tile;

void set_state(struenum state);
