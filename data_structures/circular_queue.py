class CircularQueue:
    def __init__(self,max_size):
        self.max_size = max_size
        self.queue = [None] * self.max_size
        self.front = -1
        self.rear = -1
        self.count = 0

    def __str__(self):
        items = []
        # if there is only one element in the queue
        if self.front == self.rear and not self.is_empty:
            items.append(self.queue[self.front])
        elif self.rear > self.front:
            items = [self.queue[i] for i in range(self.front,self.rear + 1)
                       if self.queue[i] is not None]
        elif self.front > self.rear:
            for i in range(self.front, self.max_size):
                items.append(self.queue[i])
                
            for j in range(0, self.rear + 1):
                items.append(self.queue[j])

        print('front:',self.front,', rear:', self.rear)
        return f'{items}'

    @property
    def is_empty(self):
        return self.front == -1 and self.rear == -1

    @property
    def is_full(self):
        return (self.rear + 1) % self.max_size == self.front

    def peek(self):
        if not self.is_empty:
            print(self.queue[self.front])

    def enqueue(self,new_item):
        if self.is_full:
            return print('queue full!')
        if self.is_empty:
            self.front, self.rear = 0, 0
        else:
            self.rear = (self.rear + 1) % self.max_size
        self.queue[self.rear] = new_item
        self.count += 1


    def dequeue(self):
        if self.is_empty:
            return print('queue empty!')

        element = self.queue[self.front]
        if self.front == self.rear:
            self.front, self.rear = -1, -1
        else:
            self.front = (self.front + 1) % self.max_size
        self.count -= 1
        print('dequeued:',element)

def main():
    q = CircularQueue(5)
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)
    q.enqueue(50)
    print(q)
    print('count:',q.count)
    q.dequeue()
    q.dequeue()
    q.dequeue()
    print(q)
    q.enqueue(60)
    print(q)
    q.enqueue(70)
    print(q)
    q.dequeue()
    print(q)
    q.dequeue()
    print(q)

if __name__ == "__main__":
    main()

