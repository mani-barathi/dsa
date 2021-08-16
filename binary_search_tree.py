SPACE = 5

class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return f'{self.data}'

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def print_tree(self,current_node,new_space):
      if current_node:
          new_space += SPACE
          self.print_tree(current_node.right,new_space)
          for i in range(SPACE,new_space):
              print(" ",end='')
          print(current_node.value)
          self.print_tree(current_node.left, new_space)

    def pre_order_traversal(self,node):
        if node:
            print(node.value,end=" ")
            self.pre_order_traversal(node.left)
            self.pre_order_traversal(node.right)

    def in_order_traversal(self,node):
        if node:
            self.in_order_traversal(node.left)
            print(node.value,end=" ")
            self.in_order_traversal(node.right)

    def post_order_traversal(self,node):
        if node:
            self.post_order_traversal(node.left)
            self.post_order_traversal(node.right)
            print(node.value,end=" ")

    def height(self,node):
        """ tree with 0 node has a height of -1
            tree with 1 node has a height of 0
        """
        if node is None:
            return -1

        lheight = self.height(node.left)
        rheight = self.height(node.right)

        if lheight > rheight:
            return lheight + 1
        return rheight + 1

    def height_iterative(self):
        if self.root is None:
            return -1

        height = -1
        queue = [self.root]
        while True:
            node_count = len(queue)
            if node_count == 0:
                return height
            height+=1

            while node_count > 0:
                current = queue.pop(0)
                if current.right:
                    queue.append(current.right)
                if current.left:
                    queue.append(current.left)
                node_count-=1
        
        return count

    def insert(self,new_node):
        if self.root == None:
            self.root = new_node
            return

        current = self.root
        while current:
            if new_node.value == current.value:
                return print(f'Unable to insert, Node with a value of {new_node.value} already exists')
            if new_node.value < current.value:
                if current.left:
                    current = current.left
                else:
                    current.left = new_node
                    return
            else:
                if current.right:
                    current = current.right
                else:
                    current.right = new_node
                    return

    def insert_recursive(self,root,new_node):
        if root is None:
            root = new_node
            return new_node

        if new_node.value == root.value:
            print(f'Unable to insert, Node with a value of {new_node.value} already exists')
            return root
        if new_node.value < root.value:
            root.left = self.insert_recursive(root.left,new_node)
        else:
            root.right = self.insert_recursive(root.right,new_node)
        return root

    def get_min_node(self,node):
        current = node
        while current.left:
                current = current.left
        return current

    def delete_node(self,node,value):
        if node is None:
            return print(f'{value} is not found')

        if value < node.value:
            node.left = self.delete_node(node.left,value)
        elif value > node.value:
            node.right = self.delete_node(node.right,value)
        else:
            # this will handle left node is None and both no left and right node are None
            if node.left is None:
                temp = node.right
                del node
                return temp
            elif node.right is None:
                temp = node.left
                del node
                return temp
            else:
                min_node = self.get_min_node(node.right)
                node.value = min_node.value
                node.right = self.delete_node(node.right,min_node.value)
        return node

    def delete(self,value):
        if self.root is None:
            return print('tree is empty')
        
        self.root = self.delete_node(self.root,value)


    def print_lvl(self,node,lvl):
        if node is None:
            return 
        if lvl == 0:
            print(node.value, end=" ")
        else:
            self.print_lvl(node.left,lvl - 1)
            self.print_lvl(node.right,lvl - 1)

    def bfs_recursive(self):
        height = self.height(self.root)
        print('bfs:',end=' ')
        for i in range(0,height+1):
            self.print_lvl(self.root,i)
        print()

    def bfs(self):
        if self.root is None: return
        print('bfs:',end=' ')
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            print(current.value,end=" ")
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        print()

    def dfs(self):
        if self.root is None: return
        print('dfs:',end=' ')
        stack = [self.root]
        while stack:
            current = stack.pop()
            print(current.value,end=" ")
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
        print()

def main():
    bs = BinarySearchTree()
    bs.delete(4)
    bs.insert(Node(10))
    bs.root = bs.insert_recursive(bs.root,Node(5))
    bs.root = bs.insert_recursive(bs.root,Node(5))
    bs.insert(Node(20))
    bs.insert(Node(30))
    bs.insert(Node(3))
    bs.print_tree(bs.root,0)
    print('height: ',bs.height(bs.root))
    print('height: ',bs.height_iterative())
    print('pre-order : ',end="")
    bs.pre_order_traversal(bs.root)
    print()
    print('in-order  : ',end="")
    bs.in_order_traversal(bs.root)
    print()
    print('post-order: ',end="")
    bs.post_order_traversal(bs.root)
    print()
    bs.bfs()
    bs.bfs_recursive()
    bs.dfs()
    bs.print_tree(bs.root,0)
    bs.delete(30)
    bs.delete(10)
    bs.delete(20)
    bs.delete(5)
    bs.delete(3)
    bs.print_tree(bs.root,0)

if __name__ == "__main__":
    main()
