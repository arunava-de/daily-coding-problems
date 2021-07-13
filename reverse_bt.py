class Tree:

    def __init__(self, v=None, l=None, r=None):
        self.val = v
        self.left = l
        self.right = r 

def reverse_tree(root):
    if root==None:
        return 

    if root.right:
        reverse_tree(root.left)
    if root.left:
        reverse_tree(root.right)

    root.left, root.right = root.right, root.left 

    return
    
root = Tree('a')
root.left = Tree('b')
root.right = Tree('c')
root.left.left = Tree('d')
root.left.right = Tree('e')
root.right.left = Tree('f')

reverse_tree(root)

root = Tree(2)
root.left = Tree(3)
root.right = Tree()
root.left.left = Tree(1)
root.left.right = Tree()