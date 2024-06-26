class MyQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def is_full(self):
        return len(self.queue) == self.capacity
    
    def enqueue(self, value):
        if not self.is_full():
            self.queue.append(value)
        else:
            raise OverflowError("Queue is full")
    
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            raise IndexError("Dequeue from empty queue")
    
    def front(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            raise IndexError("Front from empty queue")
