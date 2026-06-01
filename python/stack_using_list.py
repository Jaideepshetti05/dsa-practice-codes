class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()
    
    def peek(self):
        return self.stack[-1]

if __name__ == "__main__":
    s = Stack()
    s.push(10)
    s.push(20)
    print(f"{s.pop()} popped from stack")
