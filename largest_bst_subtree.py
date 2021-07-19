class Tree:

    def __init__(self, v, l=None, r=None):
        self.val = v
        self.left = l
        self.right = r 

def is_BST(u, min_val, max_val):

    if u==None:
        return True 

    if u.val < min_val or u.val > max_val:
        return False 

    if not is_BST(u.left, min_val, u.val-1) or not is_BST(u.right, u.val+1, max_val):
        return False 

    return True 

def size(u, s):

    if u==None:
        return 0

    if not u.left and not u.right:
        return 1 
    
    return 1 + size(u.left, s+1) + size(u.right, s+1)


def largest_BST(u):
    if u==None:
        return 0
    if not u.left and not u.right:
        return 1 
    if is_BST(u, -10**9, 10**9):
        return size(u, 0)

    return max(largest_BST(u.left), largest_BST(u.right))

root = Tree(50)
root.left     = Tree(10)
root.right     = Tree(60)
root.left.left = Tree(5)
root.left.right = Tree(20)
root.right.left = Tree(55)
root.right.left.left = Tree(45)
root.right.right = Tree(70)
root.right.right.left = Tree(65)
root.right.right.right = Tree(80)

largest_BST(root)
        