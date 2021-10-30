class Node:
    def __init__(self,value):
        self.data = value
        self.next = None


class Queue_LinkedList:
    def __init__(self):
        self.front = None
        self.rear = None
    
    @property
    def is_empty(self):
        return True if not self.front and not self.rear else False

    def count(self):
        front = self.front
        count = 0
        while front:
            count += 1
            front = front.next
        print('count:',count)

    def display(self):
        if self.is_empty:
           return print("Queue is empty")
        front = self.front
        while front:
            print(front.data,end="")
            if front.next:
                print(" --> ",end="")
            front = front.next
        print()

    def enqueue(self,new_node):
        if self.is_empty:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
            return new_node


    def dequeue(self):
        if self.is_empty:
            return print("Queue is empty")
        elif self.front == self.rear:
            dequeued = self.front
            self.front = None
            self.rear = None
            print(f"dequeued:",dequeued.data)
            return dequeued
        else:
            front = self.front
            self.front = self.front.next
            print(f"dequeued:",front.data)
            return front


def main():
    q = Queue_LinkedList()
    q.enqueue(Node(10))
    q.enqueue(Node(20))
    q.enqueue(Node(30))
    q.display()
    q.dequeue()
    q.display()
    q.enqueue(Node(40))
    q.display()
    q.count()
    q.dequeue()
    q.dequeue()
    q.display()
    q.dequeue()
    q.display()
    q.count()

if __name__ == "__main__":
    main()
