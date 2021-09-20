import sys

class MaxHeap:
    def __init__(self,max_size):
        self.max_size = max_size
        self.no_of_nodes = 0
        self.nodes = [-1] * self.max_size

    def __str__(self):
        nodes = [str(self.nodes[i]) 
                for i in range(self.no_of_nodes) if self.nodes[i] != -1]
        return 'heap: ' + ' '.join(nodes)

    def swap(self,i,j):
        self.nodes[i], self.nodes[self.parent(i)] = self.nodes[self.parent(i)], self.nodes[i]

    def parent(self,i):
        return (i - 1) // 2

    def left(self,i):
        return (2 * i) + 1

    def right(self,i):
        return (2 * i) + 2

    @property
    def is_full(self):
        return self.max_size == self.no_of_nodes

    @property
    def is_empty(self):
        return self.no_of_nodes == 0

    def insert(self, new_value):
        if self.is_full:
            return print('heap is full')

        self.no_of_nodes += 1
        i = self.no_of_nodes - 1
        self.nodes[i] = new_value

        while i!=0 and self.nodes[i] > self.nodes[self.parent(i)]:
            self.swap(i,self.parent(i))
            i = self.parent(i)

    def heapify(self, i):
        left = self.left(i)
        right = self.right(i)
        largest = i

        if left < self.no_of_nodes and self.nodes[largest] < self.nodes[left]:
            largest = left
        if right < self.no_of_nodes and self.nodes[largest] > self.nodes[right]:
            largest = right

        if largest!=i:
            self.swap(largest,i)
            self.heapify(largest)

    def extract_max(self):
        if self.is_empty:
            return -(sys.maxsize)

        if self.no_of_nodes == 1:
            self.no_of_nodes -= 1
            return self.nodes[0]

        root = self.nodes[0]
        self.nodes[0] = self.nodes[self.no_of_nodes - 1]
        self.no_of_nodes -= 1
        self.heapify(0)
        return root

    def search(self, search):
        for i in range(self.no_of_nodes):
            if self.nodes[i] == search:
                return i
        return -1

    def delete(self, value):
        i = self.search(value)
        if i == -1:
            return print(f'{value} not found')

        deleted_value = self.nodes[i]
        self.nodes[i] = sys.maxsize

        while i!=0 and self.nodes[i] > self.nodes[self.parent(i)]:
            self.swap(i,self.parent(i))
            i = self.parent(i)

        self.extract_max()
        print(f'deleted: {value}')


def main():
    h = MaxHeap(5)
    h.insert(20)
    h.insert(10)
    h.insert(30)
    print(h)
    print('extracted max:',h.extract_max())
    h.delete(10)
    print(h)


if __name__ == "__main__":
    main()

