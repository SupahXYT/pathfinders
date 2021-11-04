#include <stdlib.h>

struct __qnode {
  struct __qnode *next;
  struct __qnode *prev;

  int data;
};

typedef struct __qnode *__node;

__node __new_node(int data);
void __delete_node(__node self);

typedef struct __intern_queue {
  __node head;
} __intern_queue;

typedef struct Queue {
  __intern_queue *intern_queue;

  void (*push)(struct Queue *, int);
  int (*pop)(struct Queue *);
} Queue;

__intern_queue *__new_intern_queue(void);
void __delete_intern_queue(__intern_queue *self);
void __intern_queue_push(__intern_queue *self, int data);
int __intern_queue_pop(__intern_queue *self);

Queue newQueue(void);
void deleteQueue(Queue self);
void __Queue_push(Queue *self, int data);
int __Queue_pop(Queue *self);
