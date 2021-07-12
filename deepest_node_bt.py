class Tree:

    def __init__(self, v= None, l=None, r=None):
        self.val = v
        self.left = l
        self.right = r

def get_deepest(root):

    Q = [root]
    visited = set()
    depth = {}
    depth[root] = 1

    while Q:
        u = Q.pop(0)
        visited.add(u)

        if u.left:
            if u.left not in visited:
                Q.append(u.left)
                depth[u.left] = depth[u]+1
        if u.right:
            if u.right not in visited:
                Q.append(u.right)
                depth[u.right] = depth[u]+1

    return max(depth, key=depth.get).val
        
root = Tree(1)
root.left = Tree(2)
root.right = Tree(3)
root.left.left = Tree(4)
root.right.left = Tree(5)
root.right.right = Tree(6)
root.right.left.right = Tree(7)
root.right.right.right = Tree(8)
root.right.left.right.left = Tree(9)
