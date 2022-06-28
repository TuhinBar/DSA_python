class BinaryTreeNode():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def add_child(self,data):
        if data == self.data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left= BinaryTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right= BinaryTreeNode(data)

    def inorderTraversal(self):
        elements=[]
        if self.left:
            elements+=self.left.inorderTraversal()
        
        elements.append(self.data)

        if self.right:
            elements+=self.right.inorderTraversal()
        return elements

def buildTree(elements):
    if elements:
        root= BinaryTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root

# driver code

arr=[12,3,4,5,33,22,13,15,6]

numbers_tree=buildTree(arr)

print(numbers_tree.inorderTraversal())