class Node:

    def __init__(self, v, nxt=None):
        self.val = v
        self.next = nxt 
    
def reverse(l):

    head = Node(l[0])
    curr_node = Node(l[1])
    head.next = curr_node

    for i in range(2,len(l)):
        next_node = Node(l[i])
        curr_node.next = next_node
        curr_node = curr_node.next

    prev_node = None 
    curr_node = head 

    while next_node!=None:
        next_node = curr_node.next
        curr_node.next = prev_node 
        prev_node = curr_node 
        curr_node = next_node
    
    head = prev_node

    return head



            
        

    