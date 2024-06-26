class MyStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def is_full(self):
        return len(self.stack) == self.capacity
    
    def push(self, value):
        if not self.is_full():
            self.stack.append(value)
        else:
            raise OverflowError("Stack is full")
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("Pop from empty stack")
    
    def top(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("Top from empty stack")

# Testing the MyStack class

stack1 = MyStack(capacity=5)
stack1.push(1)
stack1.push(2)
print(stack1.is_full())  # Expected output: False
print(stack1.top())      # Expected output: 2
print(stack1.pop())      # Expected output: 2
print(stack1.top())      # Expected output: 1
print(stack1.pop())      # Expected output: 1
print(stack1.is_empty()) # Expected output: True
