class Queue:
    def __init__(self,max_size):
        self.max_size = max_size
        self.queue = [None] * self.max_size
        self.front = -1
        self.rear = -1

    def __str__(self):
        if self.is_empty:
            items = []
        else:
            items = [self.queue[i] for i in range(self.front,self.rear + 1)
                        if self.queue[i] is not None]
        print('front:',self.front,', rear:', self.rear)
        return f'{items}'

    @property
    def is_empty(self):
        return self.front == -1 and self.rear == -1

    @property
    def is_full(self):
        return self.rear == self.max_size - 1

    def count(self):
        if self.is_empty:
            count = 0
        else:
            count = self.rear - self.front + 1
        print(f'count: {count}')
    
    def peek(self):
        if not self.is_empty:
            print(self.queue[self.front])

    def enqueue(self,new_item):
        if self.is_full:
            return print('queue full!')
        if self.is_empty:
            self.front, self.rear = 0, 0
        else:
            self.rear += 1
        self.queue[self.rear] = new_item


    def dequeue(self):
        if self.is_empty:
            return print('queue empty!')

        element = self.queue[self.front]
        if self.front == self.rear:
            self.front, self.rear = -1, -1
        else:
            self.front += 1
        print('dequeued:',element)

def main():
    q = Queue(5)
    print(q)
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)
    q.enqueue(50)
    q.enqueue(60)
    print(q)
    print(q.count)
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    print(q)
    q.enqueue(60)
    print(q)

if __name__ == "__main__":
    main()

