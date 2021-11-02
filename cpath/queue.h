#include <stdlib.h>

struct node {
  struct node *next;
  int data;
};

struct node *new_node(int data);
void delete_node(struct node *self);

typedef struct queue {
  struct node *head;
  struct node *last;

  void (*push)(struct queue *, int);
  int (*pop)(struct queue *);
} queue;

queue *new_queue(void);
void delete_queue(queue *self);

void queue_push(queue *self, int data);
int queue_pop(queue *self);
