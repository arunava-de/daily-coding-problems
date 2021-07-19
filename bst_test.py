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
