import copy

class Node:

    def __init__(self, v, nxt=None):
        self.val = v
        self.next = nxt 

def reverse(head):
    if head.next==None:
        return head 

    curr = copy.deepcopy(head)
    prv = None 
    nxt = curr.next 

    while nxt!=None:
        nxt = curr.next
        curr.next = prv 
        prv = curr
        curr = nxt 

    return prv

def is_palindrome(head):

    head_rev = reverse(head)

    curr = head 
    curr_rev = head_rev

    while curr!=None or curr_rev!=None:
        if curr!=None and curr_rev==None:
            return False 
        elif curr==None and curr_rev!=None:
            return False

        if curr.val==curr_rev.val:
            curr = curr.next
            curr_rev = curr_rev.next
            continue 
        else:
            return False 

    return True

l = [1,2,3,4,3,2,1]
head = Node(l[0])
curr_node = Node(l[1])
head.next = curr_node

for i in range(2,len(l)):
    next_node = Node(l[i])
    curr_node.next = next_node
    curr_node = curr_node.next

is_palindrome(head)

l = [1,2,3,4,3,2,2]
head = Node(l[0])
curr_node = Node(l[1])
head.next = curr_node

for i in range(2,len(l)):
    next_node = Node(l[i])
    curr_node.next = next_node
    curr_node = curr_node.next

is_palindrome(head)