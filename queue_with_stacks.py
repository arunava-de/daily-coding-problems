class Stack:
    def __init__(self):
        self.stack = []
        self.length = 0
    
    def push(self, val):
        self.stack.append(val)
        self.length += 1 
    
    def pop(self):
        if self.length==0:
            print("Stack empty, can't pop")
            return 
        else:
            value = self.stack.pop(-1)
            self.length -= 1
            return value
    
class Queue:
    def __init__(self):
        self.stk = Stack()
        self.queue = Stack()
        self.length = 0
    
    def enqueue(self, val): #Here we just add to the first stack
        self.stk.push(val)
    
    def dequeue(self): #Here we need to implement FIFO logic

        if self.stk.length==0:
            print("Queue empty, can't dequeu")
            return
        while self.stk.length>0:
            self.queue.push(self.stk.pop())
        res = self.queue.pop()

        while self.queue.length>0:
            self.stk.push(self.queue.pop())

        return res

if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue()) 