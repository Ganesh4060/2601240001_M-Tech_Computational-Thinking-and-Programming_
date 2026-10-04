from dataclasses import dataclass, field
from typing import Generic, TypeVar
from collections import deque

T = TypeVar("T")


@dataclass
class Queue(Generic[T]):
    items: deque[T] = field(default_factory=deque)

    def enqueue(self, item: T) -> None:
        self.items.append(item)

    def dequeue(self) -> T:
        if not self.items:
            raise IndexError("Queue is empty")

        return self.items.popleft()

    def front(self) -> T:
        if not self.items:
            raise IndexError("Queue is empty")

        return self.items[0]

    def is_empty(self) -> bool:
        return len(self.items) == 0