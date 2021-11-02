#include "queue.h"
#include <stdio.h>

struct Qnode *new_node(int data) {
  struct Qnode *new = malloc(sizeof(struct Qnode));
  new->next = NULL, new->prev = NULL;
  new->data = data;

  return new;
}

void delete_node(struct Qnode *self) { free(self); }

queue *new_queue(void) {
  queue *new = malloc(sizeof(queue));
  new->head = NULL;

  new->push = _Queue_push;
  new->pop = _Queue_pop;

  return new;
}

void delete_queue(queue *self) {
  struct Qnode *curr = self->head;

  while (curr != NULL) {
    struct Qnode *next = curr->next;
    delete_node(curr);
    curr = next;
  }
  free(self);
}

void _Queue_push(queue *self, int data) {
  if (self->head == NULL) {
    self->head = new_node(data);
    self->head->next = self->head;
    self->head->prev = self->head;
  } else {
    struct Qnode *old = self->head;
    self->head = new_node(data);
    self->head->next = old;
    self->head->prev = old->prev;
    old->prev = self->head;
  }
}

int _Queue_pop(queue *self) {
  if (self->head->prev == NULL) {
    fprintf(stderr, "\033[0;31merror\033[0m: no more elements in queue\n");
    exit(1);
  }
  if (self->head->prev == self->head) {
    delete_node(self->head);
    self->head = NULL;
  }
  struct Qnode *popped = self->head->prev;
  self->head->prev = popped->prev;
  popped->prev->next = popped->next;
  int data = popped->data;
  delete_node(popped);

  return data;
}

void print_queue(queue *self) {
  struct Qnode *curr = self->head;

  if (curr != NULL) {
    printf("node data: %d\n", curr->data);
    curr = curr->next;
    while (curr != self->head) {
      printf("node data: %d\n", curr->data);
      curr = curr->next;
    }
  }
}
