class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return None

    def is_empty(self):
        return len(self.queue) == 0

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            return None

    def size(self):
        return len(self.queue)
    
q1 = Queue()
q1.enqueue(100)  
q2 = Queue()
q2.enqueue(200)
q3 = Queue()
q3.enqueue(300)

print(q1.dequeue())
print(q1.dequeue()) 
print(q2.dequeue())
print(q3.dequeue())    