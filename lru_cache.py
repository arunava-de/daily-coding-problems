class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None 
        self.prev = None 

class LRUCache:
    def __init__(self, n):
        self.hash = {} #Stores mappings to cache keys i.e nodes
        self.capacity = n 
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail 
        self.tail.prev = self.head 
        self.count = 0 

    def deleteNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def addToHead(self, node):
        node.next = self.head.next
        node.next.prev = node 
        node.prev = self.head 
        self.head.next = node  

    def put(self, key, val):
        if key in self.hash: #Key already present in cache, we need to bring it to the top
            node = self.hash[key]
            node.val = val
            self.deleteNode(node)
            self.addToHead(node)
        else: #Key not present in cache, need to add
            # node = self.hash[key]
            node = Node(key, val)
            self.hash[key] = node
            if self.count>self.capacity: #Here we delete last node
                del self.hash[self.tail.prev.key]
                self.deleteNode(self.tail.prev)
                self.addToHead(node)
            else:
                self.addToHead(node)
                self.count += 1
    
    def get(self, key):
        if key in self.hash:
            node = self.hash[key]
            self.deleteNode(node)
            self.addToHead(node)
            return node.val
        else:
            print("Key not present")
            return -1 



lru = LRUCache(2)
lru.put(1, 1)
lru.put(2,2)
lru.get(1)
lru.put(3,3)
lru.get(2)
lru.put(4,4)
lru.get(1)
lru.get(3)
lru.get(4)

