from re import search


class Node:
    def __init__(self, data, key ):
        self.data = data
        self.key = key
        self.left = None 
        self.right = None

    def __str__(self):
        return str(self.data)
    
class BinaryTree:
    def __init__(self, data=None, node=None):
        if node:
            self.root = node
        elif data:
            node = Node(data)
            self.root = node
        else:
            self.root = None

    def in_order(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.in_order(node.left)
        print(node,end=' ')
        if node.right:
            self.in_order(node.right)
            

    def pos_order(self,node=None):
        if node is None:
            node = self.root
        if node.left:
            self.pos_order(node.left)
        if node.right:
            self.pos_order(node.right)
        print(node)

    def height(self,node=None):
        if node is None:
            node = self.root
        hleft = 0
        hright = 0
        if node.left:
            hleft = self.height(node.left)
        if node.right:
            hright = self.height(node.right)
        if hright > hleft:
            return hright + 1
        return hleft + 1
class BinearySearchTree(BinaryTree):
    def insert(self,value):
        parent = None
        x = self.root
        while (x):
            parent = x 
            if value < x.data:
                x =  x.left
            else:
                x = x.right
        if parent is None:
            self.root = Node(value)
        elif value < parent.data:
            parent.left = Node(value)
        else:
            parent.right = Node(value)
    
    def search(self,value,node=0):
        if node == 0:
            node = self.root
        if node is None or node.data == value:
            return BinearySearchTree(node)
        if value < node.data:
            return self.search(value,node.left)
        return self.search(value,node.right)

        

    def search(self, node, key):
        if node == None or key == node.key:
            return node
        if node < node.key:
            return search(node.left, key)
        if node > node.key:
            return search(node.right, key)
        
    

    def minTree(self, node):
        while node.left != None:
            node = node.left
        return node 