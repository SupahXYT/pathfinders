#include <stdio.h>
#include <stdlib.h>

struct basic {
  int data;

  int (*set_data)(struct basic *, int);
  int (*get_data)(struct basic *);
};

struct _closure {
  void (*__call__)(struct basic *, ...);
};

static void _set_data(struct basic *self, int data) { self->data = data; }
static int _get_data(struct basic *self) { return self->data; }

int main(void) { struct basic test; }
