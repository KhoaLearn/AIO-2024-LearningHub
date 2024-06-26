
from myqueue import MyQueue

# Initialize the queue with a capacity of 5
queue1 = MyQueue(capacity=5)

# Test is_empty method
print(queue1.is_empty())

# Test is_full method
print(queue1.is_full()) 

# Test enqueue method
queue1.enqueue(1)
queue1.enqueue(2)

# Test front method
print(queue1.front())   

# Test dequeue method
print(queue1.dequeue()) 
print(queue1.front())   
print(queue1.dequeue()) 
print(queue1.is_empty())