class Tree:

    def __init__(self, v, l=None, r=None):
        self.val = v
        self.left = l
        self.right = r 

def find_max(node):

    if node==None:
        return 0 

    lmax = find_max(node.left)
    rmax = find_max(node.right)

    max_single = max(max(lmax, rmax) + node.val, node.val)

    max_sub = lmax + node.val + rmax 

    find_max.maxpath = max(max(max_single, max_sub), find_max.maxpath)
    
    return max_single # Sending this for parent call since we'll do max for other cases in parent function call 

def max_path_sum(root):

    find_max.maxpath = -10**9 
    find_max(root)

    return find_max.maxpath

root = Tree(10)
root.left = Tree(2)
root.right   = Tree(10)
root.left.left  = Tree(20)
root.left.right = Tree(1)
root.right.right = Tree(-25)
root.right.right.left   = Tree(3)
root.right.right.right  = Tree(4)

print(max_path_sum(root))