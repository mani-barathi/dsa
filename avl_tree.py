SPACE = 5

class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return f'{self.data}'

class AVLTree:
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

    def get_balance_factor(self,node):
        if not node:
            return -1
        return self.height(node.left) - self.height(node.right)

    def right_rotation(self,first):
        second = first.left
        second_right = second.right

        second.right = first
        first.left = second_right
        return second

    def left_rotation(self,first):
        second = first.right
        second_left = second.left
        
        second.left = first
        first.right = second_left
        return second

    def insert(self,node,new_node):
        if node is None:
            return new_node

        if new_node.value == node.value:
            print(f'Unable to insert, Node with a value of {new_node.value} already exists')
            return node
        elif new_node.value < node.value:
            node.left = self.insert(node.left,new_node)
        elif new_node.value > node.value:
            node.right = self.insert(node.right,new_node)

        bf = self.get_balance_factor(node)
        if bf > 1  and new_node.value < node.left.value:   # LL 
            return self.right_rotation(node)
        if bf < -1 and new_node.value > node.right.value:  # RR
            return self.left_rotation(node)
        if bf > 1  and new_node.value > node.left.value:   # LR 
            node.left = self.left_rotation(node.left)
            return self.right_rotation(node)
        if bf < -1 and new_node.value < node.right.value:  # RL 
            node.right = self.right_rotation(node.right)
            return self.left_rotation(node)

        return node


def main():
    t = AVLTree()
    t.root = t.insert(t.root,Node(5))
    t.root = t.insert(t.root,Node(10))
    t.root = t.insert(t.root,Node(20))
    t.print_tree(t.root,0)

if __name__ == "__main__":
    main()
