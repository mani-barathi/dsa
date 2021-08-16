class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.head is None:
            return 'List is empty'
        current = self.head
        while current:
            print(current.data, end=" ")
            if current.next:
                print("-->",end=" ")
            current = current.next
        return ''

    def append(self,new_node):
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def prepend(self,new_node):
            new_node.next = self.head
            self.head = new_node

    def insert(self,new_node,value):
        current = self.search(value)
        if current is None:
            return print(f'No node exists with the value of {value}')
        new_node.next = current.next
        current.next = new_node

    def delete(self,value):
        if self.head is None:
            return print('List is empty')
        
        if self.head.data == value:
            self.head = self.head.next
            return print(f'{value} is delete from the list')

        prev = self.head
        current = self.head.next
        while current:
            if current.data == value:
                prev.next = current.next
                return print(f'{value} is delete from the list')
            prev = current
            current = current.next

        print(f'{value} is not present in the list')


    def search(self,value):
        if self.head is None:
            return None

        current = self.head
        while current:
            if current.data == value:
                return current
            current = current.next
        return None

    def sort(self):
        if self.head is None:
            return None

        current = self.head
        while current:
            next_node = current.next
            while next_node:
                if next_node.data < current.data:
                    current.data, next_node.data = next_node.data, current.data
                next_node = next_node.next
            current = current.next

def main():
    l = LinkedList()
    l.delete(10)
    l.prepend(Node(10))
    l.append(Node(5))
    l.prepend(Node(20))
    l.insert(Node(15),10)
    l.insert(Node(13),11)
    print(l)
    l.sort()
    print(l)
    print(l.search(10))
    l.delete(10)
    l.delete(5)
    l.delete(20)
    print(l)

if __name__ == "__main__":
    main()
