class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.data)

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)
        if self.root == None:
            self.root = new_node
        node = self.root
        while True:
            pre_node = node
            if node.data > new_node.data:
                node = node.left
                if node == None:
                    node = new_node
                    pre_node.left = node
            elif node.data < new_node.data:
                node = node.right
                if node == None:
                    node = new_node
                    pre_node.right = node
            else: return
    def preorder(self, node):
        print(node, end=" ")
        if node.left != None:
            self.preorder(node.left)
        if node.right != None:
            self.preorder(node.right)
tree = Tree()
tree.insert(2)
tree.insert(4)
tree.insert(3)
tree.insert(1)
tree.preorder(tree.root)