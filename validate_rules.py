opposites = {'N':'S', 'S':'N', 'E':'W', 'W':'E'}

class Node:

    def __init__(self, val):
        self.val = val 
        self.neighbours =  {'N':set(), 'S':set(), 'E':set(), 'W':set()}

class Map:

    def add_rule(self, node1, direction, node2):

        for c in direction:
            if node2 in node1.neighbours[c] or node1 in node2.neighbours[opposites[c]]: # Contradicting rules
                raise Exception
            
            for node in node1.neighbours[c]: # Add derived rules for vertices which are c direction from node1, hence c direction from node2
                self.add_rule(node, c, node2)

        for c in direction:
            node2.neighbours[c].add(node1)
            node1.neighbours[opposites[c]].add(node2)

# Test 1

a = Node('a')
b = Node('b')
c = Node('c')

M = Map()

M.add_rule(a,'N',b)
M.add_rule(b, 'NE', c)
M.add_rule(c, 'N', a)

# Test 2

a = Node('a')
b = Node('b')

M = Map()

M.add_rule(a,'NW',b)
M.add_rule(a,'N',b)

# Test 3

a = Node('a')
b = Node('b')

M = Map()

M.add_rule(a,'N',b)
M.add_rule(a,'S',b)

# Test 4

a = Node('a')
b = Node('b')
c = Node('c')

M = Map()

M.add_rule(a,'N',b)
M.add_rule(b,'N',c)
M.add_rule(c,'N',a)

# Test 5

a = Node('a')
b = Node('b')

M = Map()

M.add_rule(a,'N',b)
M.add_rule(b,'E',b)



