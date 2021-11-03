#include <stdlib.h>

struct __qnode {
  struct __qnode *next;
  struct __qnode *prev;

  int data;
};

typedef struct __qnode *node;

node __new_node(int data);
void __delete_node(struct __qnode *self);

typedef struct queue {
  node head;

  void (*push)(struct queue *, int);
  int (*pop)(struct queue *);
} queue;

queue *new_queue(void);
void delete_queue(queue *self);

void __queue_push(queue *self, int data);
int __queue_pop(queue *self);
void print_queue(queue *self);
