import sys

class MinHeap:
    def __init__(self,max_size):
        self.max_size = max_size
        self.no_of_nodes = 0
        self.nodes = [-1] * self.max_size
    
    def __str__(self):
        nodes = [str(self.nodes[i]) 
                    for i in range(self.no_of_nodes) if self.nodes[i] != -1]
        return ' '.join(nodes)

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

    def insert(self, new_node):
        if self.is_full:
            return print('Heap is full')
        
        self.no_of_nodes += 1
        i = self.no_of_nodes - 1
        self.nodes[i] = new_node

        while i != 0 and self.nodes[i] < self.nodes[self.parent(i)] :
            self.swap(i,self.parent(i))
            i = self.parent(i)

    def heapify(self, i):
        left = self.left(i)
        right = self.right(i)
        smallest = i

        if left >= self.no_of_nodes and right >= self.no_of_nodes:
            return

        if self.nodes[smallest] > self.nodes[left] :
            smallest = left

        if self.nodes[smallest] > self.nodes[right] :
            smallest = right

        if smallest != i:
            self.swap(smallest,i)
            self.heapify(smallest)

    def extract_min(self):
        if self.is_empty:
            return sys.maxsize

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


    # delete based on index or value
    def delete(self, index_or_value, based = 'index'):
        index = index_or_value
        if based == 'index':
            if index < 0 or index >= self.no_of_nodes:
                return print('index out of range')

        if based == 'value':
            index = self.search(index_or_value)
            if index == -1:
              return print('value not found')

        # Actual Delete Process
        # 1. replace delete node index with a large negative value
        self.nodes[index] = -sys.maxsize -1

        # 2. decrease the index and bring to the root position
        i = index
        while i!=0 and self.nodes[i] < self.nodes[self.parent(i)]:
            self.swap(i,self.parent(i))
            i = self.parent(i)

        # 3. extract min and heapify
        self.extract_min()
        
        print(f'deleted based on {based} {index_or_value}')

    def sort(self):
        # if the array is not a min-heap, below loop will make it a min-heap
        # i = (self.no_of_nodes // 2) - 1         # get the last non-leaf node
        # while i >= 0:
        #     self.heapify(i);
        #     i -= 1
    
        sorted_nodes = [-1] * self.max_size
        for j in range(self.no_of_nodes):
            sorted_nodes[j] = self.extract_min()
        print(sorted_nodes)

def main():
    h = MinHeap(5)
    h.insert(20)
    h.insert(10)
    h.insert(30)
    print(h)
    h.extract_min()
    print(h)
    h.insert(5)
    h.insert(7)
    print(h)
    h.sort()
    print(f'Extracted Min: {h.extract_min()}')
    h.delete(10,'value') 
    h.delete(1,'index') 

if __name__ == "__main__":
    main()

