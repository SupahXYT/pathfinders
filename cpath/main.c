#include "queue.h"
#include <stdio.h>

int main(void) {
  queue *q = new_queue();

  for (int i = 0; i < 10; i++) {
    q->push(q, i);
  }

  print_queue(q);

  for (int i = 0; i < 11; i++) {
    printf("pop: %d\n", q->pop(q));
  }
}
