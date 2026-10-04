from dataclasses import dataclass, field
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass
class Stack(Generic[T]):
    items: list[T] = field(default_factory=list)

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        if not self.items:
            raise IndexError("Stack is empty")

        return self.items.pop()

    def peek(self) -> T:
        if not self.items:
            raise IndexError("Stack is empty")

        return self.items[-1]

    def is_empty(self) -> bool:
        return len(self.items) == 0