#include "queue.h"
#include <stdio.h>

node __new_node(int data) {
  node new = malloc(sizeof(struct __qnode));
  new->next = NULL, new->prev = NULL;
  new->data = data;
  return new;
}

void __delete_node(struct __qnode *self) { free(self); }

queue *new_queue(void) {
  queue *new = malloc(sizeof(queue));
  new->head = NULL;
  new->push = __queue_push;
  new->pop = __queue_pop;
  return new;
}

void delete_queue(queue *self) {
  node curr = self->head;

  while (curr != NULL) {
    node next = curr->next;
    __delete_node(curr);
    curr = next;
  }

  free(self);
}

void __queue_push(queue *self, int data) {
  if (self->head == NULL) {
    self->head = __new_node(data);
    self->head->next = self->head;
    self->head->prev = self->head;

  } else {
    node last = self->head->prev;
    node new = __new_node(data);

    last->next = new;
    new->next = self->head;
    new->prev = last;
    self->head = new;
  }
}

int __queue_pop(queue *self) {
  if (self->head == NULL) {
    fprintf(stderr, "\033[0;31merror\033[0m: no more elements in queue\n");
    exit(1);

  } else if (self->head->prev == self->head) {
    int data = self->head->data;

    __delete_node(self->head);
    self->head = NULL;
    return data;

  } else {
    node popped = self->head->prev;
    int data = popped->data;

    self->head->prev = popped->prev;
    popped->prev->next = popped->next;
    __delete_node(popped);

    return data;
  }
}

void print_queue(queue *self) {
  struct __qnode *curr = self->head;

  if (curr != NULL) {
    printf("node at %p: data: %d\n", curr, curr->data);
    curr = curr->next;
    while (curr != self->head) {
      printf("node at %p: data: %d\n", curr, curr->data);
      curr = curr->next;
    }
  }
}
