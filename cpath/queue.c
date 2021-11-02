#include "queue.h"

struct node *new_node(int data) {
  struct node *new = malloc(sizeof(struct node));
  new->data = data;
  new->next = NULL;

  return new;
}

void delete_node(struct node *self) { free(self); }

queue *new_queue(void) {
  queue *new = malloc(sizeof(queue));
  new->head = NULL, new->last = NULL;

  new->push = queue_push;
  new->pop = queue_pop;

  return new;
}

void delete_queue(queue *self) {
  struct node *curr = self->head;

  while (curr != NULL) {
    struct node *next = curr->next;
    delete_node(curr);
    curr = next;
  }
  free(self);
}

void queue_push(queue *self, int data) {
  if (self->head == NULL) {
    self->head = new_node(data);
    self->last = self->head;
  } else {
    struct node *old = self->head;
    self->head = new_node(data);
    self->head->next = old;
  }
}

int queue_pop(queue *self) {
  struct node *popped = self->last;
  int data = popped->data;
  delete_node(popped);

  return data;
}
