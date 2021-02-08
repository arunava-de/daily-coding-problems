class Stack:

    def __init__(self, l):
        self.S = l 
    
    def push(self, val):
        self.S.append(val)

    def pop(self):
        if len(self.S)==0:
            return None
        return self.S.pop()

    def max(self):
        if len(self.S)==0:
            return None
        return max(self.S)
    
    def print_stack(self):
        print(self.S)

S = Stack([1,2,3])
S.push(-1)
print(S.pop())
S.print_stack()
print(S.max())