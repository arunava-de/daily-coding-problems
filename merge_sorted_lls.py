class Node:

    def __init__(self, v=None, nxt=None):
        self.val = v
        self.next = nxt 

def make_linked_list(l):
    head = Node()
    head.val = l[0]
    curr = head 

    for i in range(1,len(l)):
        curr.next = Node(l[i])
        curr = curr.next

    return head

def print_linked_list(head):
    while head.next:
        print(head.val, end=" ")
        head = head.next


def merge_k(heads):

    curr_node = Node()
    head = curr_node 

    while True:
        curr_val = 10**9
        flag = 0
        for i in range(len(heads)):
            if heads[i]==None:
                continue
            flag = 1 # At least one linked list still remains
            if heads[i].val<curr_val:
                curr_val = heads[i].val
                curr_index = i
        
        if flag==0: #All LLs exhausted
            break

        curr_node.val = curr_val 
        heads[curr_index] = heads[curr_index].next
        curr_node.next = Node()
        curr_node = curr_node.next

        if flag==0:
            break

    return head 

h1 = make_linked_list([1,4,8])
h2 = make_linked_list([2,5,7])
h3 = make_linked_list([2,3,6,9])
h4 = make_linked_list([7])

merge_k([h1, h2, h3, h4])

        

        