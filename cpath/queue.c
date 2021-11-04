#include "queue.h"
#include <errno.h>
#include <stdio.h>
#include <stdlib.h>

extern int errno;

__node __new_node(int data) {
  __node new = malloc(sizeof(struct __qnode));
  new->next = NULL, new->prev = NULL;
  new->data = data;
  return new;
}

void __delete_node(__node self) { free(self); }

__intern_queue *__new_intern_queue(void) {
  __intern_queue *new = malloc(sizeof(__intern_queue));
  new->head = NULL;
  return new;
}

void __delete_intern_queue(__intern_queue *self) {
  __node curr = self->head;

  while (curr != NULL) {
    __node prev = curr->prev;
    prev->next = NULL;
    __node next = curr->next;
    __delete_node(curr);
    curr = next;
  }

  free(self);
}

void __intern_queue_push(__intern_queue *self, int data) {
  if (self->head == NULL) {
    self->head = __new_node(data);
    self->head->next = self->head;
    self->head->prev = self->head;
  } else {
    __node last = self->head->prev;
    __node new = __new_node(data);

    last->next = new;
    new->next = self->head;
    new->prev = last;
    self->head = new;
  }
}

int __intern_queue_pop(__intern_queue *self) {
  if (self->head == NULL) {
    fprintf(stderr, "\033[0;31merror\033[0m: "
                    "no more elements in queue\n");
    exit(-1);
  } else if (self->head->prev == self->head) {

    int data = self->head->data;
    __delete_node(self->head);
    self->head = NULL;
    return data;

  } else {
    __node first = self->head;
    int data = first->data;
    __node prev = first->prev;
    __node next = first->next;

    prev->next = next;
    next->prev = prev;
    self->head = next;

    __delete_node(first);
    return data;
  }
}

Queue newQueue(void) {
  Queue new;
  new.intern_queue = __new_intern_queue();

  new.push = __Queue_push;
  new.pop = __Queue_pop;

  return new;
}

void deleteQueue(Queue self) { __delete_intern_queue(self.intern_queue); }

void __Queue_push(Queue *self, int data) {
  __intern_queue_push(self->intern_queue, data);
}

int __Queue_pop(Queue *self) { return __intern_queue_pop(self->intern_queue); }
