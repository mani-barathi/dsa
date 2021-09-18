
class Node:
    key_count = 0
    def __init__(self,value):
        Node.key_count += 1
        self.key = Node.key_count
        self.value = value
        self.next = None


class Stack_LinkedList:
    def __init__(self):
        self.top = None
        self.count = 0

    @property
    def is_empty(self):
        return True if self.top is None else False

    def push(self,new_node):
        if self.top is None:
            self.top = new_node
        else:
            prev_top = self.top
            self.top = new_node
            self.top.next = prev_top
        self.count += 1

    def pop(self):
        if self.is_empty:
            print('Stack is Empty')
            return None

        poped = self.top
        self.top = self.top.next
        self.count -= 1
        print('poped:',poped.value)
        return poped

    def display(self):
        top = self.top
        while top:
            print(top.value,end="  ")
            top = top.next
        print()


def main():
    s = Stack_LinkedList()
    s.push(Node(10))
    s.push(Node(20))
    s.push(Node(30))
    s.push(Node(40))
    print('count:',s.count)
    s.display()
    s.pop()
    s.display()
    s.pop()
    s.display()

if __name__ == "__main__":
    main()
