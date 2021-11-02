#include <stdlib.h>

struct Qnode {
  struct Qnode *next;
  struct Qnode *prev;

  int data;
};

struct Qnode *new_node(int data);
void delete_node(struct Qnode *self);

typedef struct queue {
  struct Qnode *head;

  void (*push)(struct queue *, int);
  int (*pop)(struct queue *);
} queue;

queue *new_queue(void);
void delete_queue(queue *self);

void _Queue_push(queue *self, int data);
int _Queue_pop(queue *self);
void print_queue(queue *self);
