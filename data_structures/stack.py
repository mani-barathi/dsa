class Stack:
    def __init__(self,max_size):
        self.max_size = max_size
        self.stack = [None] * self.max_size
        self.top = -1

    def __str__(self):
        items = [n for n in range(0,self.top + 1) 
                    if self.stack[n] is not None]
        items.reverse()
        return f'{items}'

    @property
    def is_empty(self):
        return self.top == -1

    @property
    def is_full(self):
        return self.top == self.max_size

    def count(self):
        if self.is_empty:
            return print(f'count: 0')
        print(f'count: {self.top + 1}')
    
    def peek(self):
        if not self.is_empty:
            print(self.stack[self.top])

    def push(self,new_item):
        if self.is_full:
            return print('stack is full')
        if self.is_empty:
            self.top = 0
        else:
            self.top += 1
        self.stack[self.top] = new_item

    def pop(self):
        if self.is_empty:
            return print('stack is empty')
        poped = self.stack[self.top]
        self.top -= 1
        return poped

def main():
    s = Stack(5)
    s.push(0)
    s.push(1)
    print(s)
    s.pop()
    print(s)

if __name__ == "__main__":
    main()


