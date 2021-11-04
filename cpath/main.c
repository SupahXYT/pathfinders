#include "queue.h"
#include <stdio.h>

int main(void) {
  Queue que = newQueue();

  for (int i = 0; i < 10; i++) {
    que.push(i);
  }

  for (int i = 0; i < 10; i++) {
    que.pop();
  }

  /* delete_queue(que); */
}
