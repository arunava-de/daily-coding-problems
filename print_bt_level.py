class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val 
        self.left = left 
        self.right = right 

def print_levels(root):
    if root==None:
        return 

    out = []
    Q = [root]

    while Q:

        u = Q.pop(0)
        out.append(u.val)

        l = u.left
        r = u.right 

        if l and r:
            Q.append(l)
            Q.append(r)
        elif l and not r:
            Q.append(l)
        elif r and not l:
            Q.append(r)

    return out 

root = Tree(1)
root.left = Tree(2)
root.right = Tree(3)
root.right.left = Tree(4)
root.right.right = Tree(5)




