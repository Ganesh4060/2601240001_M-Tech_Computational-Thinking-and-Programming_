from stack import Stack
from queue import Queue


# Stack
stack = Stack[int]()

stack.push(10)
stack.push(20)
stack.push(30)

print("Stack:", stack.items)
print("Stack Pop:", stack.pop())
print("Stack Top:", stack.peek())


# Queue
queue = Queue[str]()

queue.enqueue("A")
queue.enqueue("B")
queue.enqueue("C")

print("Queue:", list(queue.items))
print("Queue Dequeue:", queue.dequeue())
print("Queue Front:", queue.front())