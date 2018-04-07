##                                          ##
# Implementing a Binary Tree Data Structure  #
##                                          ##


# Generally speaking, this implementation lacks parent node, which makes it harder to delete from it.
# (This node has forgotten the face of its father...) 


class binNode:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

    def add(self, node):
        if node.data >= self.data:
            if self.right == None:
                self.right = node
            else:
                self.right.add(node)
        else:
            if self.left == None:
                self.left = node
            else:
                self.left.add(node)

                
    def add_data(self, value):
        node = binNode(value)
        self.add(node)
                
    def inorder_tree_walk(self, node):
        if node != None:
            self.inorder_tree_walk(node.left)
            print(node.data)
            self.inorder_tree_walk(node.right)
            
    # works in O(h) time, where h is tree's height 
    def min(self):
        node = self
        while node.left != None:
            node = node.left
        return node
    
    def max(self):
        node = self
        while node.right != None:
            node = node.right
        return node

            
""" Inorder-Tree-Walk, starting from start_node"""
def traverse(start_node):
    if start_node != None:
        traverse(start_node.left)
        print(start_node.data)
        traverse(start_node.right)
  
'''returns node with data == elem '''
def recursive_search(node, element):
    if node == None or element == node.data:
        return node
    if element < node.data:
        return recursive_search(node.left, element)
    else:
        return recursive_search(node.right, element)

# Returns node with data == elem
def iterative_search(node, elem):
    while node != None and elem != node.data:
        if elem < node.data:
            node = node.left
        else:
            node = node.right
            
    return node

# Minimum element: (works in O(h), which is pretty obvious)
def find_min(start_node):
    while start_node.left != None:
        start_node = start_node.left
    return start_node

def find_max(start_node):
    while start_node.right != None:
        start_node = start_node.right
    return start_node


# probably a clumsy implementation
# but it's the first one i've written, so...
""" Delete operation from a tree: """
def delete_from_tree(node, key, parent):
    if key < node.data:
        delete_from_tree(node.left, key, node)
    if key > node.data:
        delete_from_tree(node.right, key, node)
    if key == node.data:
        # we can start deleting:
        # 1) if the node has no children:
        if node.left == None and node.right == None:
            if parent.left and parent.left.data == key:
                parent.left = None
            if parent.right and parent.right.data == key:
                parent.right = None
            return
        # 2) if the node has only one child:
        if node.left == None:
            if parent.left and parent.left.data == key:
                parent.left = node.right
            if parent.right and parent.right.data == key:
                parent.right = node.right
        elif node.right == None:
            if parent.right and parent.right.data == key:
                parent.right = node.left
            if parent.left and parent.left.data == key:
                parent.left = node.left
        else:
            # 3) all nodes are in place
            min_node = find_min(node.right) # finding min element in right subtree:
            node.data = min_node.data # element to replace exchanged with min_node
            delete_from_tree(node.right, min_node.data, node)# recurrently deleting the min_node from the right subtree:
            


#
# Disposable part:
#
""" Achtung, it's Testing! """
'''
tree = binNode(5)
tree.add_data(3)
tree.add_data(4)
tree.add_data(7)
tree.add_data(9)
tree.add_data(6)
#tree.inorder_tree_walk(tree)
print("Tree traverse:")
traverse(tree)
# --------------------------
print("Min: ", tree.min().data)
print("Max: ", find_max(tree).data)
num = int(input("Choose number to delete: "))
delete_from_tree(tree, num, None)
traverse(tree)
'''

""" Tree operations testing: """
tree = None
print("Commands: add, delete, traverse (a.k.a print), min, max, stop")

while True:
    command = input()
    command = command.split()
    print(command)
    if command[0] == "add":
        if not tree:
            tree = binNode(int(command[1]))
        else:
            tree.add_data(int(command[1]))
    if command[0] == "delete":
        delete_from_tree(tree, int(command[1]), None)
    if command[0] == "traverse" or command[0] == "print":
        traverse(tree)
    if command[0] == "min":
        print(tree.min().data)
    if command[0] == "max":
        print(tree.max().data)
    if command[0] == "stop" or command[0] == "exit":
        break
        

        