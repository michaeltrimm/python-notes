#!/usr/bin/python

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class Tree(object):
    def __init__(self):
        self.root = None
    
    def get_root(self):
        return self.root
    
    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.insert(value, self.root)
    
    def insert(self, value, node):
        if value < node.value:
            if node.left != None:
                self.insert(value, node.left)
            else:
                node.left = Node(value)
        else:
            if node.right != None:
                self.insert(value, node.right)
            else:
                node.right = Node(value)
    
    def find(self, value):
        if self.root is not None:
            return self.search(value, self.root)
        else:
            return none
    
    def search(self, value, node):
        if value == node.value:
            return node
        elif value < node.value and node.left is not None:
            return self.search(value, node.left)
        elif value > node.value and node.right is not None:
            return self.search(value, node.right)
    
    def delete(self):
        self.root = None
    
    def print_tree(self):
        if self.root is not None:
            self.print_node(self.root)
    
    def print_node(self, node):
        if node is not None:
            self.print_node(node.left)
            print str(node.value) + ' '
            self.print_node(node.right)
        
        
tree = Tree()
tree.add(3)
tree.add(4)
tree.add(0)
tree.add(8)
tree.add(2)
tree.print_tree()
print (tree.find(3)).value
print tree.find(10)
tree.delete()
tree.print_tree()