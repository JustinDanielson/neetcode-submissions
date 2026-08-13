class Node:
    def __init__(self, key: int, val: Any=0, prev: Node=None, next: Node=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:
    # Impl idea:
    # Use doubly linked list to implement cache, so I can have constant time insert and delete
    # without underlying object changing size.
    # Not sure how to implement LRU... maybe everytime I touch something, I make it the head?
    # Then maintain a head and tail pointer?
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.count = 0
        self.tail = self.data = Node("dummy", None, None)
        self.cache: dict[int: Node] = dict()
        
    def get(self, key: int) -> int:
        mru_node = self._pop(key)
        if mru_node:
            self._insert_at_head(mru_node)
        return mru_node.val if mru_node else -1 

    def put(self, key: int, value: int) -> None:
        mru_node = self._pop(key)
        if not mru_node:
            mru_node = Node(key, value)
        else:
            mru_node.val = value
        self._insert_at_head(mru_node)
    
    def _insert_at_head(self, mru_node: Node) -> None:
        self.cache[mru_node.key] = mru_node
        if self.count == self.capacity:
            self._pop_lru()
        # insert mru_node to head
        mru_node.next = self.data.next
        mru_node.prev = self.data
        # point neighbor nodes to mru_node
        if mru_node.next:
            mru_node.next.prev = mru_node
        mru_node.prev.next = mru_node
        self.count += 1
        if self.count == 1:
            self.tail = mru_node

    def _pop_lru(self) -> None:
        # delete lru_node and evict from cache (always tail)
        if self.count >= 1:
            lru_node = self.tail
            self.tail = lru_node.prev
            self.tail.next = None
            del self.cache[lru_node.key]
            self.count -= 1

    def _pop(self, key: int) -> Node:
        '''
        Pop node from data and return it, if it exists.
        '''
        mru_node = self.cache.get(key, None)
        # remove mru_node from list if exists
        if mru_node:
            mru_node.prev.next = mru_node.next #all nodes have prev bc of 'dummy'
            if self.tail == mru_node: # special case if mru_node is tail
                self.tail = mru_node.prev
            else: # handle middle nodes
                mru_node.next.prev = mru_node.prev
            del self.cache[mru_node.key]
            self.count -= 1
        return mru_node