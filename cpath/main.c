#include "queue.h"
#include <stdio.h>

int main(void) {
  Queue que = new_queue();

  for (int i = 0; i < 10; i++) {
    que->push(que, i);
  }

  for (int i = 0; i < 10; i++) {
    printf("pop: %d\n", que->pop(que));
  }

  delete_queue(que);
}
